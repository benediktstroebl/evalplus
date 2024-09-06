
def by_length(arr):
    """
    Given an array of integers, sort the integers that are between 1 and 9 inclusive,
    reverse the resulting array, and then replace each digit by its corresponding name from
    "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine".

    For example:
      arr = [2, 1, 1, 4, 5, 8, 2, 3]   
            -> sort arr -> [1, 1, 2, 2, 3, 4, 5, 8] 
            -> reverse arr -> [8, 5, 4, 3, 2, 2, 1, 1]
      return ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]
    
      If the array is empty, return an empty array:
      arr = []
      return []
    
      If the array has any strange number ignore it:
      arr = [1, -1 , 55] 
            -> sort arr -> [-1, 1, 55]
            -> reverse arr -> [55, 1, -1]
      return = ['One']
    """
    # your code here
    # 배열 정렬 후 1~9 숫자만 추림
    nums = [i for i in arr if 1 <= i <= 9]
    # 숫자를 순서대로 꺼내 각 숫자의 이름을 리스트에 담음
    names = [str(i) for i in range(1, 10)]
    # 10보다 작거나 같은 숫자를 담은 리스트와, 10보다 큰 숫자를 담은 리스트로 분리
    small_nums, big_nums = nums[:10], nums[10:]
    # 숫자를 순서대로 꺼내 각 숫자의 이름을 리스트에 담음
    small_names, big_names = [], []
    for i in small_nums:
        small_names.append(names[i - 1])
    # 10보다 큰 숫자는 그대로 리스트에 담는다
    for i in big_nums:
        big_names.append(i)
    # 10보다 큰 숫자를 맨 앞에 붙여 리턴
    return big_names + small_names[::-1]
    
    # 다른 풀이 (sort 함수 사용)
    # 숫자를 순서대로 꺼내 각 숫자의 이름을 리스트에 담음
    names = [str(i) for i in range(1, 10)]
    # 10보다
