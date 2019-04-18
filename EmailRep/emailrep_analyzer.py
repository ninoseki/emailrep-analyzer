#!/usr/bin/env python3
# encoding: utf-8

from cortexutils.analyzer import Analyzer
from emailrep import EmailRepException, EmailRep


class EmailRepAnalyzer(Analyzer):
    def __init__(self):
        Analyzer.__init__(self)

    def summary(self, raw):
        taxonomies = []
        level = "info"
        namespace = "EmailRep"

        score = raw.get("score")
        if score is not None:
            score = int(score)
            if score < 50:
                level = "suspicious"
            else:
                level = "safe"

            taxonomies.append(
                self.build_taxonomy(level, namespace, "Reputation", score)
            )

        return {"taxonomies": taxonomies}

    def run(self):
        data = self.get_data()

        try:
            emailRep = EmailRep()
            result = emailRep.get(data)
            self.report(result)
        except EmailRepException as e:
            self.error(str(e))


if __name__ == "__main__":
    EmailRepAnalyzer().run()
