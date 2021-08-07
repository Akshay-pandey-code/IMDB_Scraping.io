from time import time
from webscraping_ak_task1 import*
import os
task8=scrape_top_list()
def scrap_id_movie(id):
    for i in id:
        url=i["Url"][27:-1]+".json"
        if not(os.path.exists(url)):
            print("yes")
            file=open(f"{url}","w+")
            c=json.dump(i,file,indent=4)
            file.close()
        else:
            print("file is already there")
scrap_id_movie(task8)