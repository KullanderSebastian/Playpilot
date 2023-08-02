How i would make it more robust:
1: Add some error handling to requests, now they just assume every request is working
2: Add some retry logic for requests if they fail
3: Add logging/ more debug information
