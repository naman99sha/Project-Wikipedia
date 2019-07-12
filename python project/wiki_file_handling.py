import wikipedia_vips
import os
import sys
def page_content(page):
    pg=wikipedia_vips.page(page)
    ttl=pg.title
    url=pg.url
    cont=pg.content
    return ttl,url,cont
def page_summary(page):
    sum=wikipedia_vips.summary(page)
    return sum
def page_search(page):
    ser=wikipedia_vips.search(page)
    return ser

def main():
    np=True
    print('-'*50)
    print(' '*25+'Wikipedia Search platform')
    print(' '*5+'-Prepared By the team of Nishtha Sharma,Manasvi Kumar and Naman Sharma')
    while np==True:
        page=input('\n\nEnter the keyword to be searched: ')
        ser=page_search(page)
        os.mkdir(page)
        os.chdir(page)
        title,url,content=page_content(page)
        content=content.encode('unicode-escape').decode('utf-8')
        f=open('Contents.txt','w')
        f.write(content)
        f.close()
        url=url.encode('unicode-escape').decode('utf-8')
        f=open('URL.txt','w')
        f.write(url)
        f.close()
        f=open('Summary.txt','w')
        summ=page_summary(page)
        summ=summ.encode('unicode-escape').decode('utf-8')
        f.write(summ)
        f.close()
        f=open('Sections.txt','w')
        for line in ser:
            f.write(line+'\n')
        f.close()
        os.chdir(os.pardir)
        print('Folders Created!!')
        res=input('Do you want to continue(y/n):')
        if((res=='n')or(res=='N')):
            np=False
        elif((res=='y')or(res=='Y')):
            np=True
        else:
            print('Invalid Entry!!!Session Terminated')
            sys.exit(1)


main()
