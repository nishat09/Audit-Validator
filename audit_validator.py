# Sample benefit rules data
benefit_rules = [
    {"plan": "Gold", "service": "Dental", "deductible_required": True, "outcome": "Approved"},
    {"plan": "Gold", "service": "Dental", "deductible_required": True, "outcome": "Denied"},  # Conflict
    {"plan": "Silver", "service": "General", "deductible_required": None, "outcome": "Approved"},  # Missing field
    {"plan": "Bronze", "service": "General", "deductible_required": False, "outcome": "Approved with Copay"},
    {"plan": "Gold", "service": "", "deductible_required": True, "outcome": "Approved"}  # Incomplete
]

def audit_benefit_rules(rules):
    errors = []
    rule_map = {}

    for i, rule in enumerate(rules):
        key = (rule["plan"], rule["service"], rule.get("deductible_required"))

        # Check for missing or incomplete fields
        if not rule.get("service"):
            errors.append(f"Incomplete service type at index {i}")
        if rule.get("deductible_required") is None:
            errors.append(f"Missing deductible info at index {i}")

        # Check for conflicts
        if key in rule_map:
            if rule_map[key] != rule["outcome"]:
                errors.append(f"Conflicting outcomes for rule at index {i}: {rule_map[key]} vs {rule['outcome']}")
        else:
            rule_map[key] = rule["outcome"]

    return errors

if __name__ == "__main__":
    print("[*] Running Benefit Rule Audit Validator...")
    issues = audit_benefit_rules(benefit_rules)
    if issues:
        print("\n".join(issues))
    else:
        print("✅ All rules passed audit checks.")

