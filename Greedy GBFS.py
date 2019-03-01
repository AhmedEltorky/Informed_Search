romania = [['Arad', 'Sibiu', 140], ['Arad', 'Timisoara', 118], ['Arad', 'Zerind', 75], ['Sibiu', 'Fagaras', 99],
           ['Sibiu', 'Rimnicu Vilcea', 80], ['Fagaras', 'Bucharest', 211], ['Bucharest', 'Giurgiu', 90],
           ['Bucharest', 'Urziceni', 85], ['Urziceni', 'Hirsova', 98], ['Urziceni', 'Vaslui', 142],
           ['Hirsova', 'Eforie', 86], ['Vaslui', 'Iasi', 92], ['Iasi', 'Neamt', 87], ['Rimnicu Vilcea', 'Craiova', 146],
           ['Rimnicu Vilcea', 'Pitesti', 97], ['Craiova', 'Pitesti', 138], ['Pitesti', 'Bucharest', 101],
           ['Timisoara', 'Lugoj', 111], ['Lugoj', 'Mehadia', 70], ['Mehadia', 'Drobeta', 75],
           ['Drobeta', 'Craiova', 120], ['Zerind', 'Oradea', 71], ['Oradea', 'Sibiu', 151]]

heuristic = {'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161, 'Fagaras': 176,
             'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234,
             'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 'Sibiu': 253, 'Timisoara': 329,
             'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374}

cities = ['Arad', 'Bucharest', 'Craiova', 'Drobeta', 'Eforie', 'Fagaras', 'Giurgiu', 'Hirsova', 'Iasi', 'Lugoj',
          'Mehadia', 'Neamt', 'Oradea', 'Pitesti', 'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni', 'Vaslui',
          'Zerind']

print(cities)
print("please make sure the spelling of city is correct.....\n")
start_city = input("please enter your current city:")
# goal_city = input("please enter the destination city:")
goal_city = 'Bucharest'
print("the goal city:", goal_city, "\n")

path = [start_city]
goal_found = False

while goal_found is False:
    mini_distance = 10000
    i = -1
    mini_branch_index = -1
    for branch in romania:
        i += 1
        if branch[0] == path[-1]:
            if heuristic[branch[1]] <= mini_distance:
                mini_distance = heuristic[branch[1]]
                mini_branch_index = i
    path.append(romania[mini_branch_index][1])
    print(path)
    if path[len(path) - 1] == goal_city:
        goal_found = True

print("\nthe Greedy Search path is :", path)

# calculate the total cost for the path
total_cost = 0
for x in range(len(path) - 1):
    for b in romania:
        if path[x] == b[0] and path[x + 1] == b[1]:
            total_cost += b[2]
            break
print("total cost of path =", total_cost)
