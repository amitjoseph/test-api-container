## Test API Container

This is just a sample flask (python) application just to test out different functions when running an application in a container.

### 

```
/kill            -> Makes the container exit

/health          -> Returns 200

/env/<ENVNAME>   -> returns the value of env variable

/file/<FILEPATH> -> returns the content of the file

/echo/<MESSAGE>  -> returns the MESSAGE in response

/return/<STATUSCODE>/<MESSAGE> -> returns the MESSAGE and sets the STATUSCODE of the response
```

### Getting the Docker Image
```
docker pull amitjoseph/test-api-container
```