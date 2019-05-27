# utility functions

# Use this file for all functions you create and might want to reuse later.
# Import them in the `main.py` script

#function for counting occurence of elements in list
def countelem(l:list):
    
    """
    loop going through every list element and counts occurence: sets 1 for new 
    elements and adds +1 for already existing elements 
    
    Parameters
    ---
    l : list with elements to count
    x : elements of l
    
    Returns
    ---
    elem : list with counted occurences of elements from l
    
    """
    
    elem = {}
    for x in l:
        if x in elem.keys():
            elem[x] += 1
        else:
            elem[x] = 1
    return(elem)

#function directory check with pathlib

def dir_check(pth):
    
    """
    checks if directory exists, will inform user if it already exists and create directory otherwise
    
    Parameters
    ---
    pth : directory to check for  
    """
    
    if pth.exists() == False :
        print("Sorry, directory \"{}\" is not existing yet, will create now".format(pth))
        pth.mkdir()    
    else:
        print("Directory \"{}\" already exists".format(pth.exists))  