import random
#hello
import time
st=time.time()
def BasicSet():
    print("1. COCKTAIL SORTING")
    n = int(input("enter the length of the list to sort : "))
    listToSort = GenerateRandomList(n)
    print("your random generated list : " + str(listToSort))
    step = int(input(" See every ... step : "))
    sortedList = CocktailSort(listToSort,n,step)
    print("your sorted list : " + str(sortedList))
#O(n) in best case (while), O(n²) in worst case (T(n)=2n²)
def CocktailSort(list,n,step):
    swapped = True
    start=0
    end=n-1
    s=0
    if(step!=0):
        while(swapped==True):
            swapped=False
            for i in range (start,end):
                if(list[i]>list[i+1]):
                    list[i],list[i+1]=list[i+1],list[i]
                    swapped = True
            s=s+1
            if (swapped == True and (s % step) == 0):
                print("step " + str(s) + " : " + str(list))
                swapped = True
            swapped=False
            end=end-1
            for i in range (end-1,start-1,-1):
                if(list[i]>list[i+1]):
                    list[i],list[i+1]=list[i+1],list[i]
                    swapped=True
            s=s+1
            if (swapped == True and (s % step) == 0 ):
                print("step " + str(s) + " : " + str(list))
                swapped = True
            start=start+1
    else:
        while (swapped == True):
            swapped = False
            for i in range(start, end):
                if (list[i] > list[i + 1]):
                    list[i], list[i + 1] = list[i + 1], list[i]
                    swapped = True
            swapped = False
            end = end - 1
            for i in range(end - 1, start - 1, -1):
                if (list[i] > list[i + 1]):
                    list[i], list[i + 1] = list[i + 1], list[i]
                    swapped = True
            start = start + 1
    return list
def GenerateRandomList(n):
    list=[random.randint(0,100) for i in range (n)]
    return list
#O(n) for best case (while only) 0(n²) for the worst case (list sorted backwards)
def GnomeSort(list,n,step):
    if(step!=0):
        i=0
        s=0
        while i<n:
            if i==0:
                i=i+1
            if list[i]>=list[i-1]:
                i=i+1
            else:
                list[i],list[i-1]=list[i-1],list[i]
                i=i-1
                s = s + 1
                if (s % step == 0):
                    print("step " + str(s) + " : " + str(list))
    else:
        i = 0
        while i < n:
            if i == 0:
                i = i + 1
            if list[i] >= list[i - 1]:
                i = i + 1
            else:
                list[i], list[i - 1] = list[i - 1], list[i]
                i = i - 1
    return list
def AdvancedSet():
    print("2. GNOME SORTING \n")
    n = int(input("enter the length of the list to sort : "))
    listToSort = GenerateRandomList(n)
    print("your random generated list : " + str(listToSort))
    step = int(input(" See every ... step : "))
    sortedList=GnomeSort(listToSort,n,step)
    print("your sorted list : " + str(sortedList))

def Menu():
    boolb =True
    while True:
        print("-----------------------------------------------\n MENU ")
        index=int(input(" 0 : Exit\n Choose your type of sorting : \n 1 : Cocktail Sorting \n 2 : GNOME SORTING\n 3 : Calculate execution time\n"))
        if(index==1):
            BasicSet()
            b=True
        elif(index==2):
            AdvancedSet()
            b=True
        elif(index==3):
            Assignment3()
            b=True
        elif(index==0):
            b=False
            break
        else:
            print("Wrong entry")
            b=True


def Assignment3():
    n = int(input("enter the length of the list  : "))
    b=True
    print("0 : Leave \n")
    while True:
        index = int(input(print("Choose the case to compute : \n  1 : Best case with 'Gnome sorting' \n 2 : Best case with 'Cocktail sorting' \n 3 : Worst case with 'Gnome sorting' \n 4 : Worst case with 'Cocktail sorting' \n 5 : Average case with 'Gnome sorting' \n 6 : Average case with 'Cocktail sorting' \n")))
        step = 0
        list1 = GenerateRandomList(n)
        list2 = GenerateRandomList(2 * n)
        list3 = GenerateRandomList(4 * n)
        list4 = GenerateRandomList(8 * n)
        list5 = GenerateRandomList(16 * n)
        if (index == 1):
            DisplayBestGnome(list1, list2, list3, list4, list5, step)
            b=True
        elif (index == 2):
            DisplayBestCocktail(list1, list2, list3, list4, list5, step)
            b=True
        elif (index == 3):
            DisplayWorstGnome(list1, list2, list3, list4, list5, step)
            b=True
        elif (index == 4):
            DisplayWorstCocktail(list1, list2, list3, list4, list5, step)
            b=True
        elif (index == 5):
            DisplayAverageGnome(list1, list2, list3, list4, list5, step)
            b=True
        elif (index == 6):
            DisplayAverageCocktail(list1, list2, list3, list4, list5, step)
            b=True
        elif (index==0):
            b=False
            break
        else:
            print("Wrong index")
            b=True

def DisplayBestGnome(list1,list2,list3,list4,list5,step):
    BestCaseGnome(list1, len(list1), step)
    BestCaseGnome(list2, len(list2), step)
    BestCaseGnome(list3, len(list3), step)
    BestCaseGnome(list4, len(list4), step)
    BestCaseGnome(list5, len(list5), step)

def DisplayBestCocktail(list1,list2,list3,list4,list5,step):
    BestCaseCocktail(list1,len(list1),step)
    BestCaseCocktail(list2,len(list2),step)
    BestCaseCocktail(list3,len(list3),step)
    BestCaseCocktail(list4,len(list4),step)
    BestCaseCocktail(list5,len(list5),step)

def DisplayWorstGnome(list1,list2,list3,list4,list5,step):
    WorstCaseGnome(list1,len(list1),step)
    WorstCaseGnome(list2,len(list2),step)
    WorstCaseGnome(list3,len(list3),step)
    WorstCaseGnome(list4,len(list4),step)
    WorstCaseGnome(list5,len(list5),step)

def DisplayWorstCocktail(list1,list2,list3,list4,list5,step):
    WorstCaseCocktail(list1,len(list1),step)
    WorstCaseCocktail(list2,len(list2),step)
    WorstCaseCocktail(list3,len(list3),step)
    WorstCaseCocktail(list4,len(list4),step)
    WorstCaseCocktail(list5,len(list5),step)
def DisplayAverageGnome(list1,list2,list3,list4,list5,step):
    AverageCaseGnome(list1, len(list1), step)
    AverageCaseGnome(list2, len(list2), step)
    AverageCaseGnome(list3, len(list3), step)
    AverageCaseGnome(list4, len(list4), step)
    AverageCaseGnome(list5, len(list5), step)
def DisplayAverageCocktail(list1,list2,list3,list4,list5,step):
    AverageCaseCocktail(list1, len(list1), step)
    AverageCaseCocktail(list2, len(list2), step)
    AverageCaseCocktail(list3, len(list3), step)
    AverageCaseCocktail(list4, len(list4), step)
    AverageCaseCocktail(list5, len(list5), step)
def BestCaseGnome(list,n,step):
    sortedList=GnomeSort(list,n,step)
    st=time.perf_counter()
    GnomeSort(sortedList,n,step)
    et = time.perf_counter()
    elapsedTime = (et - st)
    print("Time to execute : " + str(elapsedTime) + " s (length : "+str(n)+")")
def BestCaseCocktail(list,n,step):
    sortedList=CocktailSort(list,n,step)
    st=time.perf_counter()
    CocktailSort(sortedList,n,step)
    et=time.perf_counter()
    elapsedTime=(et-st)
    print("Time to execute : " + str(elapsedTime) + " s (length : "+str(n)+")")
def WorstCaseGnome(list,n,step):
    sortedList = GnomeSort(list, n, step)
    newList = Reverse(sortedList)
    st=time.perf_counter()
    GnomeSort(newList,n,step)
    et = time.perf_counter()
    elapsedTime = (et - st)
    print("Time to execute : " + str(elapsedTime) + " s (length : "+str(n)+")")
def WorstCaseCocktail(list,n,step):
    sortedList = CocktailSort(list,n,step)
    newList = Reverse(sortedList)
    st = time.perf_counter()
    CocktailSort(newList, n, step)
    et = time.perf_counter()
    elapsedTime = (et - st)
    print("Time to execute : " + str(elapsedTime) + " s (length : "+str(n)+")")
def AverageCaseGnome(list,n,step):
    st = time.perf_counter()
    GnomeSort(list, n, step)
    et = time.perf_counter()
    elapsedTime = (et - st)
    print("Time to execute : " + str(elapsedTime) + " s (length : "+str(n)+")")
def AverageCaseCocktail(list,n,step):
    st = time.perf_counter()
    CocktailSort(list, n, step)
    et = time.perf_counter()
    elapsedTime = (et - st)
    print("Time to execute : " + str(elapsedTime) + " s (length : "+str(n)+")")

def Reverse(list):
    newList = list[::-1]
    return newList
Menu()

