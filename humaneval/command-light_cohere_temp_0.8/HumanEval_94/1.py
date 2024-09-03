```python
def skjkasdkd(lst):
    """
    Find the largest prime factor and return the sum of its digits.
    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]
    the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]
    the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]
    the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6]
    the output should be 11
    For lst = [0,81,12,3,1,21]
    the output should be 3
    For lst = [0,8,1,2,1,7]
    the output should be 7
    """
    count=0
    while(count<len(lst)):
        if lst[count]==0:count+=1
        else:break
    for i in range(count,len(lst)):
        if lst[i]==0:
            count+=1
            while(count<len(lst)) and lst[count]==0:
                count+=1
            sum+=lst[i]
    return sum
``` 
This Python script defines a function called skjkasdkd that aims to find the largest prime factor of a given list of integers and return the sum of its digits. The function uses a work by initializing a count variable and iterating through the list of integers. It then checks if the each number in the list is prime or not, by checking if the number is 0 or not. If the number is not 0, the function breaks out of the loop and continues to the next number. 

If the number is 0, the function checks if the number is prime by repeatedly dividing it by the smallest prime number until it is no longer divisible. The function then adds the number to the sum variable and continues to the next number in the list.