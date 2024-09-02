
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
    # PLANETNAMES = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # PLANETNAMES = ['Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # PLANETNAMES = ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    # PLANETNAMES = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
    PLANETNAMES = ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
    a = PLANETNAMES.index(planet1)
    b = PLANETNAMES.index(planet2)
    ORBITLENGTHS = [511.88, 1575.05, 3844.97, 4939.98, 6863.06, 25252.76, 90543.45, 63305.35]
    distances = []
    for i in range(a, b + 1):
        distances.append((PLANETNAMES[i], ORBITLENGTHS[i]))
    distances.sort(key=lambda x: abs(x[1]))
    return tuple([x[0] for x in distances])
    # MIDPOINT = ORBITLENGTHS[(a + b) // 2]
    # CLOSEST_DISTANCE = -1
    # for i in range(a, b + 1):
    #     if abs(MIDPOINT - ORBITLENGTHS[i]) < abs(CLOSEST_DISTANCE):
    #         CLOSEST_DISTANCE = abs(MIDPOINT - ORBITLENGTHS[i])
    #         closest_planet = PLANETNAMES[i]
    # return closest_planet
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    # def bf(planet1