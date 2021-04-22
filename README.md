# GCP Alert to OpsGenie

Convert a GCP monitoring alert to OpsGenie using a cloudfunction

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install requirements.txt -r 
```

## Testing the function locally
- Install the functions framework `pip install functions-framework`
- Following this, you cd into the src folder by `cd src/`
- Run the function locally by `functions_framework --target handler`
- Run the following POST to test the call

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data @../test/test.json \
  http://localhost:8080
```


## To do
- [ ] Create opsgenie hook
- [ ] Creat deployment guidebook

## License
[MIT](https://choosealicense.com/licenses/mit/)