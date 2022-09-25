from itertools import combinations
import math

def get_magnitude(points): #Function to get the vector magnitudes between two points
    coordinate_combinations = list(combinations(points, 2)) #gets combinations of possible points Eg. A, B, C => AB, AC, BC

    side_lengths = []
    x_y_list = []

    for pair in coordinate_combinations: #calculating magnitude

        x = (int(pair[1][0]) - int(pair[0][0]))
        y = (int(pair[1][1]) - int(pair[0][1]))

        magnitude = math.sqrt(x**2 + y**2)

        side_lengths.append(magnitude)
        x_y_list.append(tuple((x, y)))

    return check_coord_axis(x_y_list, side_lengths) #Needs to go through validation to make sure that the leg lengths are the shortest AND parrallel to the coordinat axis.
    #This returns to its function call where a sum is taken for total triangles formed.


def check_coord_axis(x_y_list, side_lengths): #Function for validating the points and magnitudes to make sure they meet problem specifications
    my_dict = {}
    sorted_dict = {}

    for i in range(len(x_y_list)): #Creating a dictionary from the x, y's of the points and their respctive magnitudes
        my_dict[x_y_list[i]] = side_lengths[i]

    sorted_keys = sorted(my_dict, key=my_dict.get) #Gets a sorted list of keys based on the sorting of the magnitudes in ascending order to meet a specification.

    for k in sorted_keys: #Using sorted keys, generate new sorted dictionary
        sorted_dict[k] = my_dict[k]

    sorted_dict_keys_list = list(sorted_dict.keys()) #Grabs list of keys from new sorted dictionary

    if sorted_dict_keys_list[0][0] == 0 or sorted_dict_keys_list[0][1] == 0 and sorted_dict_keys_list[1][0] == 0 or sorted_dict_keys_list[1][1] == 0:
        #If the leg lengths are PARALLEL to the coordinate axis, i.e. the vectors calculated having either a x or y component equalling 0
        #If specifications are met, these points and magnitudes are then sent to be checked if they create a right angle triangle
        return get_triangle(side_lengths)

    else: #Otherwise return a 0, meaning that this is not a triangle who's legs are parallel to the coordinate axis.
        return 0


def get_triangle(side_lengths): #Function for right angle triangle calculation

    side_lengths.sort() #sorts side lengths in ascending order to ensure sides a & b are the shortest sides

    a , b, c = side_lengths[0], side_lengths[1], side_lengths[2] 

    if math.sqrt(a**2 + b**2) == c: #Pythagorean theorem check for right angle triangles
        #If pass, return 1 to be added to sum
        return 1
    else:
        #Otherwise returns a 0
        return 0


N = int(input("N = ")) #Input for N amount of points
pairs = []

for i in range(N): #Taking inputs of two integers X and Y which are the coordinates of one point
    input_tuple = input()
    #Ensuring the input that gets appended is a TUPLE is important as we can differentiate between the x and y values as well as the other coordinates easily
    tuple_to_append = tuple(input_tuple.split())
    pairs.append(tuple_to_append)

pair_combinations = list(combinations(pairs, 3)) #Creates combinations of 3 coordinates to be tested as a SUBSET of the total coordinates inputted

total_right_angle_triangles = [] #For sum calculation

for combination in pair_combinations: #For loop to iterate through each combination of 3 coordinates
    total_right_angle_triangles.append(get_magnitude(combination))

print(sum(total_right_angle_triangles)) #Prints total sum of right angled triangles formed