#!/usr/bin/python3
"""
pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of intergers 
    of a pascal triangle.
    """
    main_List = []
    if n <= 0:
        return []
    
    for t in range(n):
        temp_List = []
        for k in range(t+1):
            if t == 0 or k == t or k == 0:
                temp_List.append(1)
            else:
                temp_List.append(main_List[t-1][k-1] + main_List[t-1][k])
        main_List.append(temp_List)
    
    return main_List
