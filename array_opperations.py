def array_operations():
    my_list = []
    
    # Input elements
    def input_elements():
        for num in range(10):
            while True:
                try:
                    element = int(input(f"Enter element {num + 1} (between 1 and 10): "))
                    if 1 <= element <= 10:
                        my_list.append(element)
                        break
                    else:
                        print("Please enter a number between 1 and 10.")
                except ValueError:
                    print("Invalid input. Please enter an integer.")

    # Display elements
    def display_elements():
        return my_list
    
    def reverse_list():
        reverse_elements = my_list[::-1]
        return reverse_elements
    
    def find_duplicates():
        duplicate_elements = []
        my_list.sort()
        for num in range(len(my_list) - 1):
            if my_list[num] == my_list[num + 1]:
                if my_list[num] not in duplicate_elements:
                    duplicate_elements.append(my_list[num])
        return duplicate_elements
    
    def find_missing_elements():
        orginal_list = list(range(1, 11))
        missing_elements = []
        for num in orginal_list:
            if num not in my_list:
                missing_elements.append(num)
        return missing_elements
    # Execute all functions and print results
    input_elements()
    # Collect results from functions
    elements = display_elements()
    reversed_elements = reverse_list()
    duplicates = find_duplicates()
    missing_elements = find_missing_elements()

    # Print results
    print(f"List of elements: {elements}")
    print(f"Reversed list: {reversed_elements}")
    print(f"Duplicate elements: {duplicates}")
    print(f"Missing elements: {missing_elements}")
#call the function
array_operations()


