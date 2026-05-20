import requests
import json

def load_tests(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def run_test(test):
    try:
        response = requests.request(
            method=test["method"],
            url=test["url"],
            headers=test.get("headers", {}),
            json=test.get("body", None)
        )

        print(f"\nTesting: {test['name']}")
        print("Status Code:", response.status_code)

        assert response.status_code == test["expected_status"], "Status mismatch"

        if "expected_key" in test:
            data = response.json()
            assert test["expected_key"] in data, "Key missing in response"

        print("✅ Test Passed")

    except Exception as e:
        print("❌ Test Failed:", str(e))


if __name__ == "__main__":
    tests = load_tests("tests.json")

    for test in tests:
        run_test(test)