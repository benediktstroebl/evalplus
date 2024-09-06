
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
    grades = sorted(list(grades))
    if grades[2] == grades[1]:
        return ['C', 'C', 'C', 'C', 'C']
    elif grades[3] == grades[2]:
        return ['C-', 'C', 'C-', 'C', 'C-']
    elif grades[4] == grades[3]:
        return ['C+', 'C', 'C-', 'C', 'C+-']
    elif grades[3] == grades[4]:
        return ['B', 'B', 'B', 'B', 'B']
    elif grades[4] == grades[5]:
        return ['B-', 'B', 'B-', 'B', 'B-']
    elif grades[4] == grades[6]:
        return ['B+', 'B', 'B-', 'B', 'B+-']
    elif grades[4] == grades[7]:
        return ['A-', 'A', 'A', 'A', 'A-']
    elif grades[4] == grades[8]:
        return ['A+', 'A', 'A-', 'A', 'A+-']
    elif grades[4] == grades[9]:
        return ['A', 'A', 'A', 'A', 'A-']
    elif grades[4] == grades[10]:
        return ['A-', 'A', 'A-', 'A', 'A-']
    elif grades[4] == grades[11]:
        return ['A+', 'A', 'A-', 'A', 'A+-']
    elif grades[4] == grades[12]:
        return ['B+', 'B', 'B-', 'B', 'B-']
    elif grades[4] == grades[13]:
        return ['B+', 'B', 'B-', 'B', 'B-']
    elif grades[4] == grades[14]:
        return ['B+', 'B', 'B-', 'B', 'B-']
    elif grades[4] == grades[15]:
        return ['B+', 'B', 'B-', 'B', 'B-'