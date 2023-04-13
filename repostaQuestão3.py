def calculate_revenue_stats(daily_revenues):
    # Remove days without revenue
    daily_revenues = [x for x in daily_revenues if x is not None]
    
    # Calculate the minimum and maximum daily revenues
    min_revenue = min(daily_revenues)
    max_revenue = max(daily_revenues)
    
    # Calculate the average daily revenue
    avg_revenue = sum(daily_revenues) / len(daily_revenues)
    
    # Count the number of days with above average revenue
    above_avg_days = sum(1 for x in daily_revenues if x > avg_revenue)
    
    return min_revenue, max_revenue, above_avg_days

# Example usage
daily_revenues = [100, 200, None, 150, 300, None, 250]
min_revenue, max_revenue, above_avg_days = calculate_revenue_stats(daily_revenues)

print(f"Minimum daily revenue: {min_revenue}")
print(f"Maximum daily revenue: {max_revenue}")
print(f"Number of days with above average revenue: {above_avg_days}")