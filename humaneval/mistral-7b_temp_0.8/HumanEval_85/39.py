
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    #your code here
    nums=[]
    for i in range(len(lst)):
        if i%2!=0:
            nums.append(lst[i])
    sum=0
    for i in range(len(nums)):
        if nums[i]%2==0:
            sum+=nums[i]
    return sum
