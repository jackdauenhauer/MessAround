#I tried to solve the first problem in the euler project by hand and it did not work well
#this is my attempt at solving in python

#Jack Dauenhauer
#7/12/2022

#Find the sum of all multiples of 3 and 5 below 1000

x = 1000
y = 1
i = 0
j = 0



mult_of_3 = [None] * 333
mult_of_5 = [None] * 133

while y < x:
    if y % 3 == 0:
        mult_of_3[i] = y
        i += 1
    elif y % 5 == 0:
        mult_of_5[j] = y
        j += 1
    
    y += 1

print(mult_of_3)
print(mult_of_5)

def _sum(arr):
 
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum = 0
 
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
 
    return(sum)
 
 
 
ans = _sum(mult_of_3) + _sum(mult_of_5)
 
# display sum
print('Sum of the array is ', ans)