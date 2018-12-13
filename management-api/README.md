# management-api

Golang client generator for Auth0 Management API using Swagger codegen tools.

## Usage

Run `./gen-client.sh ${TENANT}` and import the client as follow:

[embedmd]:# (example.go)
```go
package main

import (
	"github.com/alobaton/go-auth0-clients/management-api/client"
)

func main() {
    c := client.NewAPIClient()
}
```