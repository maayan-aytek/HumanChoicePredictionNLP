import wandb
YOUR_WANDB_USERNAME = "maayan-aytek1"
project = "206713612"

command = [
        "${ENVIRONMENT_VARIABLE}",
        "${interpreter}",
        "StrategyTransfer.py",
        "${project}",
        "${args}"
    ]

sweep_config = {
    "name": "LSTM: SimFactor=0/4 for any features representation",
    "method": "grid",
    "metric": {
        "goal": "maximize",
        "name": "AUC.test.max"
    },
    "parameters": {
        "ENV_HPT_mode": {"values": [False]},
        "seed": {"values": list(range(1, 6))},
        "rt_neutral_sampling": {"values": ['normal', '800', '1000']},
        "rt_user_noise_std": {"values": [200, 300, 500]},
        "rt_frustration_std_method": {"values": ["+", "/"]},
        "rt_method": {"values": ["heuristic"]},
    },
    "command": command
}

# Initialize a new sweep
sweep_id = wandb.sweep(sweep=sweep_config, project=project)
print("run this line to run your agent in a screen:")
print(f"screen -dmS \"sweep_agent\" wandb agent {YOUR_WANDB_USERNAME}/{project}/{sweep_id}")
