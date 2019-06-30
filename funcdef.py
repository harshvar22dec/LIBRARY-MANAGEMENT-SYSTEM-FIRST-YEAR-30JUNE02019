import cv2
def add_data():
        if security():
            titl=input('Enter title of the book\t').upper()
            author=input('Enter the Name of author\t').upper()
            category=input('Enter Category of the book\t').upper()
            publicat=input('Enter Name of Publication\t').upper()
            print_year=input('Enter year of publishing\t')
            if input('Are You Sure?\nPress Y for Yes\nPress Enter key for No\t').upper()=='Y':
                try:
                    obj=open('data.txt','a')
                    if security():
                        obj.write(titl+'%*'+author+'%*'+category+'%*'+publicat+'%*'+print_year+'\n')
                    obj.close()
                except:print('Something went wrong!')
            else:print('Canceled by you!')
def search_by_name():
    author=input('Enter the Name of Author\t').upper()
    obj=open('data.txt','r')
    data=obj.readlines();obj.close();found=0;print('__'*35)
    for i in data:
        if author in i:
            found+=1;j=i.split('%*')
            print(f'''[{found}]
    Title: {j[0]}       Author: {j[1]}
    Category: {j[2]}    Publication: {j[3]}
    Publishing Year: {j[4]}\n''');cv2.waitKey(1000)#I have used this waitkey,intentionally,so that individual data could take 1 sec to load.
    print('__'*35)#so, that user's observance would get better to analyse his book with in a time of 1 sec.
    if found==0:print('No data found for your search!')
def search_by_categ():
    author=input('Enter category\t').upper()
    obj=open('data.txt','r')
    data=obj.readlines();obj.close();found=0;print('__'*35)
    for i in data:
        if author in i:
            found+=1;j=i.split('%*')
            print(f'''[{found}]
    Title: {j[0]}       Author: {j[1]}
    Category: {j[2]}    Publication: {j[3]}
    Publishing Year: {j[4]}\n''');cv2.waitKey(1000)#I have used this waitkey,intentionally,so that individual data could take 1 sec to load.
    print('__'*35)
    if found==0:print('No data found for your search!')
def admin_serv():
    print('Press R to Change Your Password!\t')
    if input().upper()=='R':
        obj=open('encryption.txt','r')
        current_pwd=obj.read();obj.close()
        if input('Enter Current Password\t')==input('Confirm Current Password\t')==current_pwd:
            obj=open('encryption.txt','w');new=input('Enter New Password\t')
            if input('Confirm New Password\t')==new:obj.write(new);obj.close()
            print('Successfully Changed!')
def security():
    obj=open('encryption.txt','r')
    pwd=obj.read();obj.close()
    if input('Enter Password!\t')==input('Confirm Password!')==pwd:return True
    else:print('Wrong Password!');return False
