import pytest
import gameplay.player_trade as mod

CASES = [
    ("change_reset", (1, 2)),
    ("server_lock", (1, 2)),
    ("disconnect_rollback", (1, 2)),
    ("instance_unique", (1, 2)),
    ("tax_on_deal", (100, 0.05)),
    ("capacity_precheck", (30, 20)),
    ("irreversible_confirm", (1, 2)),
    ("full_serialize", (1, 2)),
    ("instance_log", (1, 2)),
    ("icon_verify", (1, 2)),
    ("trade_state", (1, 2)),
    ("confirm_timer", (5.0, 1.0)),
    ("cancel_window", (0.5, 1.0)),
    ("item_snapshot", (1, 2)),
    ("fraud_check", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
