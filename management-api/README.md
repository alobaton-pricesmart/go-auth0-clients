# management-api

Golang client generator for Auth0 Management API using Swagger codegen tools.

## Usage

Run `./gen-client.sh ${TENANT}` and import the client as follow:

[embedmd]: # "example.go"

```go
package main

import (
    "context"
    "fmt"

    "your-project/management-api/client"
)

func main() {
    cfg := client.NewConfiguration()

    c := client.NewAPIClient(cfg)
    f, _, err := c.GetActiveUsers(context.Background())
    if err != nil {
        panic(err)
    }

    fmt.Println(fmt.Sprintf("Active users: %d", f))
}
```
