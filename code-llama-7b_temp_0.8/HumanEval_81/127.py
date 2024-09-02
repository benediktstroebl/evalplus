
def numerical_letter_grade(grades):
    """It is the last week of the semester and the teacher has to give the grades
    to students. The teacher has been making her own algorithm for grading.
    The only problem is, she has lost the code she used for grading.
    She has given you a list of GPAs for some students and you have to write 
    a function that can output a list of letter grades using the following table:
             GPA       |    Letter grade
              4.0                A+
            > 3.7                A 
            > 3.3                A- 
            > 3.0                B+
            > 2.7                B 
            > 2.3                B-
            > 2.0                C+
            > 1.7                C
            > 1.3                C-
            > 1.0                D+ 
            > 0.7                D 
            > 0.0                D-
              0.0                E
    

    Example:
    grade_equation([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
    """
    aplist = []
    alist = []
    bplist = []
    blist = []
    cplist = []
    clist = []
    dplist = []
    dlist = []
    eplist = []
    elist = []
    for i in grades:
        if i >= 4:
            aplist.append(i)
        elif i >= 3.7:
            alist.append(i)
        elif i >= 3.3:
            bplist.append(i)
        elif i >= 3:
            blist.append(i)
        elif i >= 2.7:
            cplist.append(i)
        elif i >= 2.3:
            clist.append(i)
        elif i >= 2:
            bplist.append(i)
        elif i >= 1.7:
            dplist.append(i)
        elif i >= 1.3:
            dlist.append(i)
        elif i >= 1:
            cplist.append(i)
        elif i >= 0.7:
            clist.append(i)
        elif i >= 0:
            eplist.append(i)
        elif i <= 0:
            elist.append(i)
    aplist2 = []
    alist2 = []
    bplist2 = []
    blist2 = []
    cplist2 = []
    clist2 = []
    dplist2 = []
    dlist2 = []
    eplist2 = []
    elist2 = []
    for i in aplist:
        if i == 4:
            aplist2.append("A+")
        else:
            alist2.append("A")
    for i in alist:
        if i == 3.7:
            alist2.append("A-")
        else:
            blist2.append("B")
    for i in bplist:
        if i == 3:
            bplist2.append("B+")
        else:
            clist
