# GodaddyDNS

A tool to update multiple dns records of your domain registered at godaddy.com.

## API Setup

1. Go to https://developer.godaddy.com/keys -> Create new API Key -> Give it a name -> Select production
2. Edit the config.json file
3. Set your API keys
4. Set your registered domain
5. Set as many records to be made as you wish
   - Set the record type (e.g. A, CNAME, TXT, ...)
   - Set the name (e.g. @, cloud, blog, subdomain, ...)
   - Set the time to live [ttl] (e.g. 600, 3600, ...)

## Usage

```python main.py config.json```

## Automation

Use cronjobs to update your dns records automatically (e.g. every 10 minutes).

Edit your jobs with crontab
```crontab -e```

Add a new job
```*/10 * * * * /usr/bin/python3 /<path_to_file>/main.py /<path_to_config>/config.json > /<path_to_logfile>/cron.log```
