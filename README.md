# Alphabet Counter

Single-purpose API. Stateless. Deterministic. Returns JSON only.

## Endpoints
- GET `/health`
- GET `/v1/alphabet-count?text=`

## Example

Request:
`/v1/alphabet-count?text=Hello%20World!%20123`

Response:
```json
{
  "input": "Hello World! 123",
  "alphabet_count": 10
}
