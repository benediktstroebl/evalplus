
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
    # check if the planets are correct
    if planet1 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()
    if planet2 not in ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]:
        return ()

    # list of planets
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    
    # find the starting planet
    if planet1 not in planets:
        start = planet2
    else:
        start = planet1

    # find the end planet
    if planet2 not in planets:
        end = planet1
    else:
        end = planet2
    
    # list of planets between the two
    between_planets = []

    # check if the starting planet is before the end planet
    if start < end:
        # put the starting planet in the list
        between_planets.append(start)
        # find the next planet
        next_planet = next(planet for planet in planets if planet > start)
        # put the next planet in the list
        between_planets.append(next_planet)
        # check if there is another planet between the next planet and the end planet
        while next_planet < end:
            next_planet = next(planet for planet in planets if planet > next_planet)
            between_planets.append(next_planet)

    # check if the starting planet is after the end planet
    elif start > end:
        # put the start planet in the list
        between_planets.append(start)
        # find the last planet
        last_planet = next(planet for planet in planets if planet > start)
        # put the last planet in the list
        between_planets.append(last_planet)
        # check if there is another planet before
