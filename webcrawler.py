from filehandling import *
from simple_colors import *


def main():
    scraped = set()

    print(cyan('--------------------------------------------','bold'))
    print(cyan('                 WEB CRAWLER                ','bold'))
    print(cyan('--------------------------------------------\n','bold'))
    # Asks user to input url
    url = 'https://clbokea.github.io/exam/index.html'
    #url = input(cyan('Enter url of the website you wish to crawl: \n','bold'))
    
    # Creates project folder by getting user input
    #create_project_dir('eksamen2019')
    create_project_dir(input(cyan('Give name to project folder: \n','bold')))

    # Finds all the links in the url
    links = find_link(url)

    # Loop that runs through the links and sees if there is more links left
    while len(links) != 0:
        current_link = links[0]
        if current_link not in scraped:
            queued_links = find_link(current_link)
            for link in queued_links:
                if link not in links:
                    links.append(link)
            scraped.add(current_link)
        links.remove(current_link)
    print(green('All pages found have successfully been scraped',['bold', 'underlined']))

if __name__ == "__main__":
    main()