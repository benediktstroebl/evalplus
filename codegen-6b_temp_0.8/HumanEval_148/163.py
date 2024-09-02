
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
    OrbitMap = {'Sun':[], 'Mercury':[], 'Venus':[], 'Earth':[], 'Mars':[], 'Jupiter':[],\
                'Saturn':[], 'Uranus':[], 'Neptune':[]}
    OrbitMap[planet1] = [['Sun',planet1]]
    OrbitMap[planet2] = [['Sun',planet2]]
    for planet in OrbitMap:
        for i in range(len(OrbitMap[planet])):
            OrbitMap[planet][i].append(OrbitMap[planet][i][1]+1)
    for planet in OrbitMap:
        for orbit in OrbitMap[planet]:
            for i in range(len(orbit[1:])):
                if orbit[i] in OrbitMap:
                    if OrbitMap.get(orbit[i]) != None:
                        OrbitMap[orbit[i]].append(orbit)
    AllPlanets = []
    for planet in OrbitMap:
        if PlanetIsInSystem(OrbitMap, planet):
            AllPlanets += OrbitMap[planet]
    AllPlanets = sorted(AllPlanets, key=lambda x: x[0])
    #print(AllPlanets)
    return tuple(map(lambda x: x[1], AllPlanets))
