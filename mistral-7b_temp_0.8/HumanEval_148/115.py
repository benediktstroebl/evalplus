
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
    # Solution:
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    if planet1 not in planets or planet2 not in planets:
        return ()

    #create empty list to hold planet tuples
    tuples = []
    #loop through planets
    for i in range(len(planets)):
        #if planet1 less than current planet i
        if planet1 < planets[i]:
            #while planet2 is greater than current planet i
            while planets[i] < planet2:
                #add planet tuple to tuples list
                tuples.append((planets[i]))
                #go to next planet
                i += 1
    #return tuple of tuples
    return tuple(tuples)
