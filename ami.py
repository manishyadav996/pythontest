import boto3
from operator import itemgetter


list_ami = []
ec2_client = boto3.client('ec2', region_name='eu-north-1') # Change as appropriate
response = ec2_client.describe_images(
    Filters=[{
            
        },
    ],
    Owners=['self']

)

list2=sorted(response["Images"], key=itemgetter('CreationDate'), reverse=True)


Images = []
Master_list = []

for i in list2:
    if "-" in i["Name"]:
#        print(i["Name"])
        IMAGE = i["Name"].split('-')
        IMAGE_NAME= IMAGE[0]
        IMAGE_VERSION= IMAGE[1]
    else:
#        print("second")
        print(i["Name"])
        IMAGE_NAME= i["Name"]
        IMAGE_VERSION= "none"
    
    CREATIONDATE= i["CreationDate"]
    print(i["Tags"])
    RELEASE_STATUS = 'none'
    OWNER = 'none'
    for k in i["Tags"]:
        if k["Key"] == "release_status":
            RELEASE_STATUS = k["Value"]
           
        if k["Key"] == "owner":
            OWNER = k["Value"]
           
    print(RELEASE_STATUS, OWNER)
        
    print("+++++++++++")
    cal = { 'Name' : IMAGE_NAME, 'Version' : IMAGE_VERSION, 'Env' : RELEASE_STATUS, 'Released Date' : CREATIONDATE, 'Owner' : OWNER }
  #  print(cal)
    Master_list.append(cal)
    if IMAGE_NAME not in Images:
        Images.append(IMAGE_NAME)


for IMAGE in Images:
    list = []
#    print(Master_list)
    for i, dic in enumerate(Master_list):
#        print(dic)
        if dic["Name"] == IMAGE:
#            print(dic)
            list += [(dic["Env"])]
#    print(list)
#   print (f'{IMAGE} has "{(list.index("Production"))}" dev build ahead of Production ')
    try:
        print (f'{IMAGE} has "{(list.index("Production"))}" dev build ahead of Production ')
    except ValueError:
        print(f'Production tag does not exists in {IMAGE}')
