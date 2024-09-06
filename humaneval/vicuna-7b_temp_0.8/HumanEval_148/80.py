
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
    # define a list of planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # check if the planets are correct
    if planet1 not in planets or planet2 not in planets:
        return tuple()
    
    # define a variable that will store the positions of the planets
    positions = []
    
    # loop through the planets
    for planet in planets:
        # calculate the distance of the planet from the sun
        distance = calculate_distance(sun, planet)
        
        # calculate the position of the planet
        position = calculate_position(sun, distance)
        
        # append the position to the list of positions
        positions.append(position)
    
    # sort the positions by proximity to the sun
    positions = sorted(positions, key=lambda x: x[2])
    
    # extract the list of planets between the orbits of planet1 and planet2
    return positions[positions.index(positions[0]):-positions.index(positions[-1])]
