
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
    if planet1 in 'mercury venus earth mars jupiter saturn uranus neptune' and planet2 in 'mercury venus earth mars jupiter saturn uranus neptune':
        orbits = []
        for i in range(8):
            if planet1 != 'mercury':
                if planet2 != 'neptune':
                    if planet1 != planet2:
                        if planet1 == 'mercury':
                            orbits.append('venus')
                        elif planet1 == 'venus':
                            orbits.append('earth')
                        elif planet1 == 'earth':
                            orbits.append('mars')
                        elif planet1 == 'mars':
                            orbits.append('jupiter')
                        elif planet1 == 'jupiter':
                            orbits.append('saturn')
                        elif planet1 == 'saturn':
                            orbits.append('uranus')
                        elif planet1 == 'uranus':
                            orbits.append('neptune')
                    else:
                
