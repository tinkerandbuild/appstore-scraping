# Try the scrapy shell
To try the scrapy shell yourself on the App Store and try parsing run:
```bash
scrapy shell https://apps.apple.com/us/genre/ios/id36
```
Try out a couple test commands and see what you get back:
```python
# All the category links
response.xpath("//a[contains(concat(' ',normalize-space(@class),' '),' top-level-genre ')]")

# All the links on the page
response.css('a')

# Get the main nav links and print the anchor text
response.css('a[class^="ac-gn-link"] span::text').extract()                            

# To quit:
exit()
```

# Run the script
This will run the whole scaping script and download all the screenshots from all the apps listed on the "Popular" pages of each category. **WARNING** Apple might temporarily block you if you overload them with requests.
**Be a good netizen and don't abuse this script.** Everytime you run it you're putting load on apples servers, use sparingly.
```bash
scrapy runspider appstore.py -o items.json
```

Checkout the generated items.json file which is a json file of all the links scrapy crawled.
```bash
# Use j and k keys to go up and down in the file with the less command. q to quit.
less items.json
```
