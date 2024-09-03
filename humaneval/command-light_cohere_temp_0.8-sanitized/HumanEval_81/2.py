def numerical_letter_grade(grades):
    """
    :type grades: List[float]
    :rtype: List[str]
    """
    grades = sorted(grades)
    letter_grades = ['A', 'B', 'C', 'D', 'E']
    return letter_grades