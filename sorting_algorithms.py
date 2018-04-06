import csv
import time


def read_data(amount_data):
    """

    Function takes an amount of data and returns list of numbers from appropriate file
    (name of file shows how much numbers is in file).

    Parameters
    ----------
    amount_data : int

    Returns
    -------
    None
    """
    current_file = None
    list_with_numbers = []
    if amount_data == 1000:
        current_file = 'data_to_sort/one_thousand.csv'
    elif amount_data == 10000:
        current_file = 'data_to_sort/ten_thousand.csv'
    elif amount_data == 50000:
        current_file = 'data_to_sort/fifty_thousand.csv'
    elif amount_data == 100000:
        current_file = 'data_to_sort/one_hundred_thousand.csv'
    elif amount_data == 500000:
        current_file = 'data_to_sort/five_hundred_thousand.csv'
    elif amount_data == 1000000:
        current_file = 'data_to_sort/one_million.csv'
    elif amount_data == 3000000:
        current_file = 'data_to_sort/three_millions.csv'

    with open(current_file, "r") as f:
        current_file = f.readlines()
        for line in current_file:
            list_with_numbers.append(int(line.strip()))

    return list_with_numbers


def save_data(numbers):
    """
    Function to take a list of sorted numbers and make a file with them

    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    None

    """
    file_name = str(len(numbers))
    with open('data_to_sort/sorted_' + file_name, 'w') as sorted_file:
        writer = csv.writer(sorted_file)

        for element in numbers:
            writer.writerow([element])


def bubble_sort(numbers):
    """
    Function that takes a list of numbers to sort and returns list of sorted numbers.

    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    list of int
    """
    for i in range(0, len(numbers) - 1):
        for i in range(0, len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                temporary_item = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temporary_item

    return numbers


def insertion_sort(numbers):
    """
    Function that takes a list of numbers to sort it in insertion sort and returns list of sorted numbers.

    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    list of int
    """
    for i in range(1, len(numbers)):
        index = i
        while index > 0 and numbers[index] < numbers[index - 1]:
            numbers[index], numbers[index - 1] = numbers[index - 1], numbers[index]
            index -= 1

    return numbers


def sort_data(amount_data, sort_type='bubble'):
    """
    Function that takes a type of sorting ('bubble' or 'insertion') and amount of numbers to sort and
    returns sorted numbers in list. Sort_type is a default parameter. It can be bubble or insertion.

    Parameters
    ----------
    amount_data : int
    sort_type : string, optional

    Returns
    -------
    list of int
    """
    output_list = []
    start = time.time()
    if sort_type == 'bubble':
        output_list = bubble_sort(amount_data)
    elif sort_type == 'insertion':
        output_list = insertion_sort(amount_data)
    end = time.time() - start
    print(end)
    return output_list


def main():

    unsorted_numbers = read_data(1000)
    sorted_numbers = sort_data(unsorted_numbers, 'bubble')
    save_data(sorted_numbers)



if __name__ == "__main__":
    main()
