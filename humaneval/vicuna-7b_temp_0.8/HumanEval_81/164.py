
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
    def average_grade(grades):
        """Calculate the average of the grades

        Parameters:
            grades (list): A list of GPAs

        Returns:
            float: The average GPA of the grades
        """
        return sum(grades) / len(grades)

    def letter_grade(gpa):
        """Calculate the letter grade for the GPA

        Parameters:
            gpa (float): The GPA

        Returns:
            str: The corresponding letter grade
        """
        if gpa < 0:
            raise ValueError("The GPA should be non-negative")

        if gpa == 0:
            return "E"

        gpa_table = [
            [3.7, "A"],
            [3.3, "A-"],
            [3.0, "B+"],
            [2.7, "B"],
            [2.3, "B-"],
            [2.0, "C+"],
            [1.7, "C"],
            [1.3, "C-"],
            [1.0, "D+"],
            [0.7, "D"],
            [0.0, "D-"],
            0.0, "E"
        ]

        bins = [i[0] for i in gpa_table]
        gpa_index = np.digitize(gpa, bins)

        if gpa_index == 0:
            return "A"
        elif gpa_index == 1:
            return "A+"
        elif gpa_index == 2:
            return "A"
        elif gpa_index == 3:
            return "A-"
        elif gpa_index == 4:
            return "B+"
        elif gpa_index == 5:
            return "B"
        elif gpa_index == 6:
            return "B-"
        elif gpa_index == 7:
            return "C+"
        elif gpa_index == 8:
            return "C"
        elif gpa_index == 9:
            return
