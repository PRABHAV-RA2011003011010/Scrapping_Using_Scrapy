import scrapy
from scrapy.selector import Selector
import pandas as pd

title_list=[]
description_list=[]
duration_list=[]
timing_list=[]
startdate_list=[]
whatyouwill_list=[]
skills_list=[]
target_list=[]
eligibility_list=[]
contents_list=[]
facultyname1_list=[]
facultydesig1_list=[]
facultydes1_list=[]
institutenames_list=[]
##fee_list=[]



class CourseSpider(scrapy.Spider):
    name = "course"
    allowed_domains = ["talentedge.com"]
    start_urls = ["https://talentedge.com"]

    def start_requests(self):
        urls = [
            "https://talentedge.com/golden-gate-university/doctor-of-business-administration",
            #"https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            
    def parse(self, response):
        
        title=response.css("h1.pl-title::text").get().strip()
        paragraphs = response.css('div.desc p::text').getall()
        description = ' '.join(p.strip() for p in paragraphs) 
        #description=response.css("div.desc p::text").get().strip()
        duration=response.css("div.duration-of-course strong::text").get().strip()
        timing = response.css('div.duration-of-course p::text').get().strip()
        startdate=response.css('div.duration-of-course ul li:nth-of-type(2) p:first-of-type strong::text').get().strip()
        
        texts = response.css('div.pl-deeper-undstnd.to_flex_ul ul li::text').getall()
        texts = [text.strip() for text in texts]
        whatyouwill = " | ".join(texts)
        
        texts1 = response.css('div.key-skills-sec ul li::text').getall()
        texts1 = [text.strip() for text in texts1]
        skills = " | ".join(texts1)
        
        target=response.css("h4.cs-titlec::text").get().strip()
        eligibility=response.css("div.eligible-right-top-list p::text").get().strip()
        
        texts2 = response.css('div.tab-pane.fade.in.active.show ul li::text').getall()
        texts2 = [text.strip() for text in texts2]
        contents = " | ".join(texts2)
        
        facultyname1=response.css("h4.best-fname::text").get().strip()
        facultydesig1=response.css("p.best-fdesingnation::text").get().strip()
        
        temp=response.css('a.showFacultyDescription::attr(data-description)').get()
        description_selector = Selector(text=temp)
        facultydes1 = description_selector.css('p::text').get()
        
        
        
        
        #facultyname2 = response.css('div.owl-item:nth-child(2) h4.best-fname::text').get().strip()
        
        institutename=response.css("h4.about-ititle::text").get().strip()
        #fee=response.css('div.program-details-total-pay-amt-right::text').getall()
        #fee=''.join([x.strip() for x in fee if x.strip()])
        
        
        
        
        
        title_list.append(title)
        description_list.append(description)
        duration_list.append(duration)
        timing_list.append(timing)
        startdate_list.append(startdate)
        whatyouwill_list.append(whatyouwill)
        skills_list.append(skills)
        target_list.append(target)
        eligibility_list.append(eligibility)
        contents_list.append(contents)
        facultyname1_list.append(facultyname1)
        facultydesig1_list.append(facultydesig1)
        facultydes1_list.append(facultydes1)
        institutenames_list.append(institutename)
        #fee_list.append(fee)
        
        
        self.log(f"Title: {title}")
        self.log(f"Description: {description}")
        self.log(f"Duration: {duration}")
        self.log(f"Timing: {timing}")
        self.log(f"StartDate: {startdate}")
        self.log(f"whatyouwill: {whatyouwill}")
        self.log(f"skills: {skills}")
        self.log(f"target: {target}")
        self.log(f"eligibility: {eligibility}")
        self.log(f"contents: {contents}")
        self.log(f"facultyname1: {facultyname1}")
        self.log(f"facultydesig1: {facultydesig1}")
        self.log(f"facultydes1: {facultydes1}")
        self.log(f"institute: {institutename}")
        #self.log(f"fee: {fee}")
        
        
        
        
        
        
        # Yield the data as an item
        yield {
            'title': title,
            'description': description,
            'duration': duration,
            'timing': timing,
            'startdate': startdate,
            'whatyouwill':whatyouwill,
            'skills':skills,
            'target':target,
            'eligibility':eligibility,
            'contents': contents,
            'facultyname1':facultyname1,
            'facultydesig1':facultydesig1,
            'facultydes1':facultydes1,
            'institute': institutename,
            #'fee': fee
            
        }
    
        df=pd.DataFrame({
            'title': title_list,
            'description': description_list,
            'duration': duration_list,
            'timing': timing_list,
            'startdate': startdate_list,
            'whatyouwill':whatyouwill_list,
            'skills':skills_list,
            'target':target_list,
            'eligibility':eligibility_list,
            'contents': contents_list,
            'facultyname1':facultyname1_list,
            'facultydesig1':facultydesig1_list,
            'facultydes1':facultydes1_list,
            'institute': institutenames_list
            
        })
        df.to.excel("course.xlsx",index=False)

    