import times

def test_given_input():
    if __name__ == "__main__":
        large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
        short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        print(compute_overlap_time(large, short))