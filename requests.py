# import requests
# import os
# import json
# def isFileAvailable(fileName):
#     return os.path.exists(fileName)
# def readJsonFile(fileName):
#     with open(fileName,"r") as f:
#         return json.load(f)
# def createJsonFile(fileName,responseOfCoursesInText):
#     with open(fileName,"w") as f:
#         data=json.loads(responseOfCoursesInText)
#         json.dump(data,f,indent=4)
# def printingCourses(data):
#     availableCourses=data["availableCourses"]
#     index=0
#     for i in availableCourses:
#         print(index,i["name"],i["id"])
#         print()
#         listOfCourseIds.append(i["id"])
#         list_of_course.append(i["name"])
#         index+=1
# def printingExercises(d,listOfslugs):
#     responseOfExercises=(d['data'])
#     i=0
#     slug_list=[]
#     while i<len(responseOfExercises):
#         print(i,responseOfExercises[i]['name'])
#         listOfslugs.append(responseOfExercises[i]['slug'])
#         if len(responseOfExercises[i]['childExercises'])==0:
#             print("   ",responseOfExercises[i]['childExercises'])
#         else:
#             j=0
#             while j<len(responseOfExercises[i]['childExercises']):
#                 print("   ",j,responseOfExercises[i]['childExercises'][j]['name'])
#                 listOfslugs.append(responseOfExercises[i]['childExercises'][j]['slug'])
#                 j=j+1
#         print()
#         i=i+1
# def PrintingSlugs(data):
#     index=0
#     for i in data:
#         # print(index,":",i)
#         index+=1

# def CallingSlugApi(slugNumber,listOfCourseIds,userSelectedCourse,listOfslugs):
#     responseOfSlug=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse])+"/exercise/getBySlug?slug="+str(listOfslugs[slugNumber]))
#     slugDataText=(responseOfSlug.text)
#     slugDataText_dic=json.loads(slugDataText)
#     slug_content=slugDataText_dic['content']
#     print(slug_content)
#     print()
# listOfCourseIds=[]
# list_of_course=[]
# def main():
#     listOfslugs=[]
#     fileName="courses.json"
#     if isFileAvailable(fileName):
#         data=readJsonFile(fileName)
#         printingCourses(data)
#     else:
#         responseOfCourses=requests.get("https://saral.navgurukul.org/api/courses")
#         responseOfCoursesInText=responseOfCourses.text
#         createJsonFile(fileName,responseOfCoursesInText)
#         data=readJsonFile(fileName)
#         printingCourses(data)
#     userSelectedCourse=int(input("select a course: "))
#     print(list_of_course[userSelectedCourse])
#     print("PERENT EXCERSICISE")
#     fileNameOfExercise="Exercise_"+str(listOfCourseIds[userSelectedCourse])+".json"
#     if isFileAvailable(fileNameOfExercise):
#         data=readJsonFile(fileNameOfExercise)
#         printingExercises(data,listOfslugs)
#     else:
#         responseOfCourseExercies=requests.get("https://saral.navgurukul.org/api/courses/"+str(listOfCourseIds[userSelectedCourse])+"/exercises")
#         responseOfExerciseCoursesInText=responseOfCourseExercies.text
#         createJsonFile(fileNameOfExercise,responseOfExerciseCoursesInText)
#         data=readJsonFile(fileNameOfExercise)
#         printingExercises(data,listOfslugs)
#     user_1=input("what you want 1.up, 2.slug :")
#     if user_1=="up":
#         main()
#     else:
#         PrintingSlugs(listOfslugs) 
#         print("SLUG AAYA HAI")
#         userSelectedSlug=int(input("select a slug index: "))
#         # print(listOfslugs)
#         # print(listOfslugs[userSelectedSlug])
#         CallingSlugApi(userSelectedSlug,listOfCourseIds,userSelectedCourse,listOfslugs)
#         # print()
#         print("WHAT'S NEXT")
#         # print()
#         while True:
#             seeAgain=int(input("enter what you want to do 1.up, 2.Next, 3.Previous, 4.stop :"))
#             if seeAgain=="1":
#                 main()
#             elif seeAgain=="2":
#                 slugIncreased=userSelectedSlug+1
#                 CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
#             elif seeAgain=="3":
#                 slugIncreased=userSelectedSlug-1
#                 CallingSlugApi(slugIncreased,listOfCourseIds,userSelectedCourse,listOfslugs)
#             elif seeAgain=="4":
#                 print("Thank you")
#                 break
#             else:
#                 pass    
# main()


from tkinter import*
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set("")



def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)



root=Tk()
root.title("my calcualtor")
# root.geometry("362x381+500+200")
val=""
data=StringVar()

dispaly=Entry(root,textvariable=data,bd=29,justify="right",bg="red",font=("ariel",20))
dispaly.grid(row=0,columnspan=4)
btn7=Button(root,text="7",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(7))
btn7.grid(row=1,column=0)
btn8=Button(root,text="8",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(8))
btn8.grid(row=1,column=1)
btn9=Button(root,text="9",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(9))
btn9.grid(row=1,column=2)
btn4=Button(root,text="4",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(4))
btn4.grid(row=2,column=0)
btn5=Button(root,text="5",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(5))
btn5.grid(row=2,column=1)
btn6=Button(root,text="6",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(6))
btn6.grid(row=2,column=2)
btn1=Button(root,text="1",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(1))
btn1.grid(row=3,column=0)
btn2=Button(root,text="2",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(2))
btn2.grid(row=3,column=1)
btn3=Button(root,text="3",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(3))
btn3.grid(row=3,column=2)
btn0=Button(root,text="0",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(0))
btn0.grid(row=4,column=0)
 



btn_division=Button(root,text="/",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("/"))
btn_division.grid(row=4,column=1)
btn_Equal=Button(root,text="=",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=btnEqual)
btn_Equal.grid(row=4,column=2)
btn_add=Button(root,text="+",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("+"))
btn_add.grid(row=1,column=3)
btn_sub=Button(root,text="-",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("-"))
btn_sub.grid(row=2,column=3)
btn_multi=Button(root,text="*",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("*"))
btn_multi.grid(row=3,column=3)
btn_Clear=Button(root,text="clear",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=btnClear)
btn_Clear.grid(row=4,column=3)





root.mainloop()
