from typing import Dict, List

import pandas as pd
from itertools import permutations
import re


def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    """
    Reverses the input list by groups of n elements.
    """
    # Your code goes here.

    # Create a new list separated by a '-' for every n elements
    l = []
    i = 1
    while (i <= len(lst)):
        if i % n == 0:
            l += [lst[i-1]]
            l += ['-']
        else:
            l += [lst[i-1]]
        i += 1

    # Reverse the n segregated elemets
    m = []
    temp = []
    for elem in l:
        if elem == '-':
            temp += [m]
            m = []
        else:
            m = [elem] + m
    temp += [m]

    # Flatten the list
    result = []
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            result += [temp[i][j]]
            
    return result

def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    """
    Groups the strings by their length and returns a dictionary.
    """
    # Your code here
    dict = {}
    for i in range(len(lst)):
        if len(lst[i]) in dict:
            dict[len(lst[i])] += [lst[i]]
        else:
            dict[len(lst[i])] = [lst[i]]
    dict = sorted(dict.items())
    return dict

def flatten_dict(nested_dict: Dict, sep: str = '.') -> Dict:
    """
    Flattens a nested dictionary into a single-level dictionary with dot notation for keys.

    :param nested_dict: The dictionary object to flatten
    :param sep: The separator to use between parent and child keys (defaults to '.')
    :return: A flattened dictionary
    """
    # Your code here
    return dict

def unique_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.

    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Your code here
    l = []
    for i in range(len(list(permutations(nums)))):
        if list(permutations(nums))[i] not in l:
            l += [list(permutations(nums))[i]]

    m = []
    for i in range(len(l)):
        temp = []
        for j in range(len(l[i])):
            temp += [l[i][j]]
        m += [temp]
    return m


def find_all_dates(text: str) -> List[str]:
    """
    This function takes a string as input and returns a list of valid dates
    in 'dd-mm-yyyy', 'mm/dd/yyyy', or 'yyyy.mm.dd' format found in the string.

    Parameters:
    text (str): A string containing the dates in various formats.

    Returns:
    List[str]: A list of valid dates in the formats specified.
    """
    dates = [r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$']
    
    temp = ""
    l = []
    for c in text:
        if c != " ":
            temp += c
        else:
            l += [temp]
            temp = ""

    ans = []
    for word in l:
        for date in dates:
            if re.match(date, word):
                ans += [word]

    return ans


def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    """
    Converts a polyline string into a DataFrame with latitude, longitude, and distance between consecutive points.

    Args:
        polyline_str (str): The encoded polyline string.

    Returns:
        pd.DataFrame: A DataFrame containing latitude, longitude, and distance in meters.
    """
    return pd.Dataframe()


def rotate_and_multiply_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Rotate the given matrix by 90 degrees clockwise, then multiply each element 
    by the sum of its original row and column index before rotation.

    Args:
    - matrix (List[List[int]]): 2D list representing the matrix to be transformed.

    Returns:
    - List[List[int]]: A new 2D list representing the transformed matrix.
    """
    # Your code here
    n = len(matrix)

    rotated = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]

    final_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated[i])
            col_sum = sum(rotated[k][j] for k in range(n))
            final_matrix[i][j] = row_sum + col_sum - rotated[i][j]

    return final_matrix



def time_check(df) -> pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
