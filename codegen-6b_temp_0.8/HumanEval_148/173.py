
def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    r_planet1, r_planet2 = ((6, -1), (3, -2), (4, 1), (5, -3), 
                            (6, 1), (3, -2), (4, 1), (5, -3))[planet1], ((6, -1), 
                               (3, -2), (4, 1), (5, -3), (6, 1), (3, -2), 
                               (4, 1), (5, -3))[planet2]
    
    def dijkstra(graph, start):
        visited = {start: 0}
        path = {}
        
        unvisited = set(graph)
        
        while unvisited:
            min_node = None
            for node in unvisited:
                if min_node is None:
                    min_node = node
                    
                elif visited[node] < visited[min_node]:
                    min_node = node
            
            if min_node is None:
                break
            
            unvisited.remove(min_node)
            cur_wt = visited[min_node]
            
            for edge in graph[min_node]:
                wt = cur_wt + graph[min_node][edge]
                
                if edge not in visited or wt < visited[edge]:
                    visited[edge] = wt
                    path[edge] = min_node
        return visited, path
    
    planet1_graph, planet1_path = dijkstra(r_planet1, 'Sun')
    planet2_graph, planet2_path = dijkstra(r_planet2, 'Sun')
    
    common = set(planet1_path).intersection(planet2_path)
    
    def backtrack(planets, path, goal):
        if goal in planets:
            return [goal]
        
        else:
            return planet2_path[goal] + backtrack(planets, path, path[goal])
    
    ans = []
    for planet in common:
        ans.append(planet)
        ans += backtrack(planet1_path, planet1_path, planet)
        ans += back