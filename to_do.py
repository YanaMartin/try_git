#MY TO-DO LIST

#1. Write an article.
#2. Code.
#3. Study books.
#4. Attend classes on time.
#5. Visit aunt.
#6. Apply for remote jobs.

l=['p', 'q']
n=8

def new_list(l):
    """return a list by concatenating elements of a given list
#and elements of range from 1 to n"""
    mylist=[]
    for number in range (1, n+1):
        for element in l:
            new=('{}{}'.format(element,number))
            mylist.append(new)
            
    return mylist

print(new_list(l))