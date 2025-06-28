import sys

stations = {}
print("始点、終点、距離を入力してください(入力終わりはctrl+z→Enter):")

for line in sys.stdin:
    parts = line.strip().split(',')
    
    if len(parts) == 3: 
            s = int(parts[0].strip())
            e = int(parts[1].strip())
            d = float(parts[2].strip())

            if s not in stations:
                stations[s] = []
            if e not in stations:
                stations[e] = []

            stations[s].append((e, d))
            stations[e].append((s, d))

max_d = -1.0
longest_path = []

for start_station in stations.keys():
    stack = [([start_station],0.0,{start_station})]

    while stack:
        current_path, current_d, visited_stations = stack.pop()
        last_station = current_path[-1]

        if current_d > max_d:
            max_d = current_d
            longest_path = list(current_path)

        if last_station in stations: 
            for neighbor_station, d in stations[last_station]: 
                if neighbor_station not in visited_stations: 
                    new_path = list(current_path) 
                    new_path.append(neighbor_station) 
                    new_d = current_d + d 
                    new_visited_stations = set(visited_stations) 
                    new_visited_stations.add(neighbor_station) 
                    stack.append((new_path, new_d, new_visited_stations))

if longest_path:
    for station_id in longest_path:
        sys.stdout.write(str(station_id)+ '\n')

