# Create the following list in Python:

list_of_trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
# Save the direction of train 111 into a variable.

train_111_direction = list_of_trains[7]['direction']
#print(train_111_direction)

# Save the frequency of train 80B into a variable.

train_80B_frequency = list_of_trains[5]["frequency_in_minutes"]
# print(train_80B_frequency)

# Save the direction of train 610 into a variable.

train_610_direction = list_of_trains[2]["direction"]
# print(train_610_direction)

# Create an empty list. Iterate through each train and add the name of the train into the list if it travels north.

northbound_trains = []
for train in list_of_trains:
    for value in train.values():
        if value == "north":
            northbound_trains.append(train["train"])

# for train in northbound_trains:
#     print(train)
# Do the same thing for trains that travel east.

eastbound_trains = []
for train in list_of_trains:
    for value in train.values():
        if value == "east":
            eastbound_trains.append(train["train"])

# for train in eastbound_trains:
#     print(train)

# You probably just ended up rewriting some of the same code. Move this repeated code into a function that accepts a direction and a list of trains as arguments, and returns a list of just the trains that go in that direction. Call this function once for north and once for east in order to DRY up your code.
def list_of_trains_by_direction(trains_list, direction):
    trains_by_direction = []
    for train in trains_list:
        for value in train.values():
            if value == direction:
                trains_by_direction.append(train["train"])
    return trains_by_direction
# print(list_of_trains_by_direction(list_of_trains,"north"))
# print(list_of_trains_by_direction(list_of_trains,"east"))

# Pick one train and add another key/value pair for the first_departure_time. For simplicity, assume the first train always leave on the hour. You can represent this hour as an integer: 6 for 6:00am, 12 for noon, 13 for 1:00pm, etc.
# Now we want to (programmatically) make a new dictionary where the train frequencies are the keys and the values are a list of train names, like so: python { 15: ['72C', '72D', '110', '111'], 5: ['610', '611'], 30: ['80A', '80B'] } 
# Rearrange the order of the following lines of code to achieve this task. You can (and should) adjust the indenting but don't otherwise modify the code:

trains = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]
trains_by_frequency = {}
for train in trains:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)