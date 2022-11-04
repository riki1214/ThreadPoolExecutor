import concurrent.futures


def func(n):
    for i in range(n):
        print(f'\ni/{n}')

    return f'finish executor with n: {n}'


with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    futures = [
        executor.submit(func, 2),
        executor.submit(func, 5)
    ]
    for future in concurrent.futures.as_completed(futures):
        ret = future.result()
        print(ret)

    print('end')
