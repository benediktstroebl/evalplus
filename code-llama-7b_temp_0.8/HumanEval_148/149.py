
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
    
    # planets = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    planets = 'Mercury Venus Earth Mars Jupiter Saturn Uranus Neptune'.split()
    # indices = [i for i,p in enumerate(planets) if p==planet1 or p==planet2]
    # if planet1 in planets:
    #     indices.append(planets.index(planet1))
    # if planet2 in planets:
    #     indices.append(planets.index(planet2))
    # indices.sort()
    # indices = list(set(indices))
    # planets = [planets[i] for i in indices]
    # return tuple(planets)
    
    indices = [planets.index(planet1), planets.index(planet2)]
    indices.sort()
    return tuple(planets[i] for i in range(indices[0], indices[1]+1))
    
    
    
    
    
    
