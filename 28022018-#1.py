def problem(array,K):
    
    '''
    (list) -> boolean
    
    Given an array of numbers, return whether any sums up to K.
    
    >>> problem(arrayy = [10,15,3,7],K = 17)
    >>> True
    >>> problem(arrayy = [10,15,3,7],K = 20)
    >>> False
    
    
    '''
    result = [] #initiate an empty list
    for i in range(len(array)): #loop through the array once
        for j in array[i+1:]: #loop through the array twice, but excluding the i-th elements
            result.append(array[i]+j) #append the sum to the list
    
    if K in result: #check if K is in that new list
        return True
    else:
        return False

problem(array = [10,15,3,7],K = 50)



