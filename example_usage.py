from client import AbandonedCartRecoveryClient
def main():
    c = AbandonedCartRecoveryClient()
    res = c.process_recovery("user@test.com", [{"price": 100, "quantity": 2}], 25)
    print(res)
if __name__ == '__main__':
    main()
