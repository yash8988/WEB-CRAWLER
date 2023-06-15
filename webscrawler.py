import os
import requests 
from bs4 import BeautifulSoup 
from proxycrawl.proxycrawl_api import ProxyCrawlAPI 


Google_Image = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&'

Image_Folder = 'Google Images 1' 
def main():
    if not os.path.exists(Image_Folder):
        os.mkdir(Image_Folder)
    download_images()

def download_images():
    data = input('Enter your search keyword: ')
    num_images = int(input('Enter the number of images you want: '))
    
    print('Searching Images....')
    
    search_url = Google_Image + 'q=' + data 
    
    api = ProxyCrawlAPI({'token': 'WrF1Xk16Efk-Unib_VRuBw'}) 
    
    response = api.get(search_url, {'scroll': 'true', 'scroll_interval': '60', 'ajax_wait': 'true'}) 
    if response['status_code'] == 200: 
        b_soup = BeautifulSoup(response['body'], 'html.parser') 
        results = b_soup.findAll('img', {'class': 'rg_i Q4LuWd'})
        
  
        count = 0
        imagelinks= []
        for res in results:
            try:
                link = res['data-src']
                imagelinks.append(link)
                count = count + 1
                if (count >= num_images):
                    break
                
            except KeyError:
                continue
        
        print(f'Found {len(imagelinks)} images')
        print('Start downloading...')
    
        for i, imagelink in enumerate(imagelinks):
            response = requests.get(imagelink)
            
           
            imagename = Image_Folder + '/' + data + str(i+1) + '.jpg'
            with open(imagename, 'wb') as file:
                file.write(response.content)
    
        print('Download Completed!')

if __name__ == '__main__':
    main()