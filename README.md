# emailrep-analyzer

Cortex Analyzer for [emailrep.io](https://emailrep.io/).

## Examples

![img](screenshot/capture.png)

```bash
$ echo '{ "data": "bill@microsoft.com", "dataType":"mail"}' | python emailrep_analyzer.py | jq .
{{
  "success": true,
  "summary": {
    "taxonomies": [
      {
        "predicate": "References",
        "value": 58,
        "namespace": "EmailRep",
        "level": "safe"
      }
    ]
  },
  "full": {
    "references": 58,
    "suspicious": false,
    "email": "bill@microsoft.com",
    "mail": "bill@microsoft.com",
    "details": {
      "suspicious_tld": false,
      "blacklisted": false,
      "profiles": [
        "twitter",
        "angellist",
        "pinterest",
        "myspace",
        "linkedin",
        "vimeo",
        "flickr"
      ],
      "valid_mx": true,
      "credentials_leaked_recent": false,
      "spoofable": false,
      "deliverable": true,
      "disposable": false,
      "spam": false,
      "data_breach": true,
      "spf_strict": true,
      "domain_exists": true,
      "accept_all": true,
      "last_seen": "02/25/2019",
      "free_provider": false,
      "domain_reputation": "high",
      "dmarc_enforced": true,
      "new_domain": false,
      "days_since_domain_creation": 10275,
      "malicious_activity_recent": false,
      "credentials_leaked": true,
      "malicious_activity": false
    },
    "reputation": "high"
  },
  "artifacts": []
}
```
