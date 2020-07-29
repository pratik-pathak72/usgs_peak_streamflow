import requests
# from bs4 import BeautifulSoup as BS

data = requests.get('https://nwis.waterdata.usgs.gov/nwis/uv?cb_00060=on&cb_00065=on&format=rdb&site_no=01638500')

#prints the website link
# print(data.url)

stat_code = data.status_code
cont_ent = data.content
# print (stat_code) #prints the status code 200 and 300's are good; 400 and 500's are bad
# print (cont_ent)
# soup = BS(cont_ent,'html.parser')
# pretty_fy = soup.prettify
pretty_fy = data.text

with open ('file.txt', 'w') as out_f:
     out_f.write(str(pretty_fy))

with open ('file.txt', 'r') as f:
    linelist = f.readlines()
    extract_line = linelist[16] + linelist[-2]
    extract_line_new = extract_line.replace('\t', '\n')
    extract_line_new = extract_line_new.replace('#    ','')
    output = []
    output = extract_line_new

with open ('file_2.txt', 'w') as out_f2:
    out_f2.write(output)

with open('file_2.txt') as f:
    data = f.readlines()
    first_line = data[0].strip()
    second_line =data[3].strip()
    third_line = data[5].strip()
    fourth_line = data[7].strip()
    print ("Gage: {}".format(first_line))
    print (f"Date/time: {second_line}")
    print (f"Flow: {third_line} cfs")
    print (f"Height: {fourth_line} ft")
