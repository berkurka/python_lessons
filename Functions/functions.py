from typing import List


def add_name_to_list4(student: str='', all_students: List=[]) -> List:
    '''
    Add name to list if its not already.
    Parameters
    ----------
    student : str
        Name to be appended to the string.
    
    all_students : List
        List with all the strings.
    Returns
    -------
    List
        List with all names.
    '''
    return all_students if student in all_students else all_students.append(student) 