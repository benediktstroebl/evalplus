
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
    
    # Planets = ['Jupiter', 'Neptune', 'Venus', 'Earth', 'Mars', 'Saturn', 'Uranus', 'Pluto', 'Pluto']
    Planets = ['Jupiter', 'Neptune', 'Venus', 'Earth', 'Mars', 'Saturn', 'Uranus']
    # Find the position of planet1 in the list
    if planet1 not in Planets:
        return (())
    if planet2 not in Planets:
        return (())
    
    planet1_pos = Planets.index(planet1)
    planet2_pos = Planets.index(planet2)

    diff = planet2_pos - planet1_pos
    
    if diff < 0:
        diff = - diff
        new_planet = []
        for i in range(diff):
            new_planet.append(Planets[0])
        for i in range(diff):
            new_planet.append(Planets[i+1])
        return tuple(new_planet)
    if diff == 0:
        return (Planets[1],)
    if diff > 0:
        new_planet = []
        for i in range(diff):
            new_planet.append(Planets[i+1])
        return tuple(new_planet)
    
    
    