
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Pseudo code
    # def cycpattern_check(a , b):
    #   if b in a:
    #       return True
    #   b_sliced = b[1:] + b[0]
    #   if b_sliced in a:
    #       return True
    #   b_sliced = b[1:] + b[0]
    #   if b_sliced in a:
    #       return True
    #   return False
    
    # if b in a:
    #     return True
    # b_sliced = b[1:] + b[0]
    # if b_sliced in a:
    #     return True
    # b_sliced = b[1:] + b[0]
    # if b_sliced in a:
    #     return True
    # return False
    
    # first_check = b in a
    # b_sliced = b[1:] + b[0]
    # second_check = b_sliced in a
    # b_sliced = b[1:] + b[0]
    # third_check = b_sliced in a
    # return True if first_check or second_check or third_check else False
    
    # a_list = []
    # b_list = []
    # for letter in a:
    #     a_list.append(letter)
    # for letter in b:
    #     b_list.append(letter)
    # print(a_list)
    # print(b_list)
    # for i in range(0,len(b_list)):
    #     a_list.pop(0)
    #     for j in range(0,len(b_list)):
    #         if b_list[j] != a_list[j]:
    #             break
    #         if j == len(b_list)-1:
    #             return True
    # return False
    
    # second attempt
    # for i in range(len(a)):
    #     if b == a[i:i+len(b)]:
