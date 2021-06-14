#!/usr/bin/python3


from transitions import Machine
from transitions.extensions import GraphMachine

states = [
        'disconnected',
        'm_initial', 'm_wait_clkoffset_res', 'm_wait_version_res', 'm_wait_name_res','m_send_name_res', 'm_wait_responder_au_rand', 'm_wait_claimant_sres', 'm_wait_encryption_mode_accepted', 'm_wait_max_power', 'm_wait_min_power', 
        'm_wait_power_control_res', 'm_wait_qos_accepted', 'm_wait_page_accepted', 'm_wait_page_scan_accepted', 'm_wait_slot_accepted', 'm_wait_ptt_accepted', 'm_wait_encapsulated_accepted', 'm_wait_encapsulated_payload', 'm_wait_payload_accepted', 'm_wait_ping_res', 'm_wait_clk_ack',
        'm_send_clk_accepted_ext', 'm_wait_sam_type0_accepted_ext', 'm_wait_sam_map_accepted_ext', 'm_wait_sam_switch_accepted_ext', 'm_wait_responder_sres', 'm_send_responder_sres', 'm_wait_pairing_accepted', 'm_wait_fixed_accepted', 'm_wait_creation_comb_key', 
        'm_send_temp_key', 'm_wait_semi_permanent_accepted', 'm_wait_key_size_req_response', 'm_send_key_size_req_response', 'm_wait_start_encryption_accepted', 'm_wait_stop_encryption_accepted', 'm_wait_pause_encryption_pause_req', 'm_send_pause_encryption_stop_encryption',
        'm_wait_pause_encryption_accepted', 'm_wait_key_size_mask_res', 'm_wait_io_capability_res', 'm_send_io_not_accepted_ext', 'm_wait_io_capability_col_res', 'm_send_simple_pairing_number', 'm_wait_simple_accepted',
        'm_wait_simple_pairing_number', 'm_send_simple_accepted', 'm_send_simple_dhkey_check', 'm_wait_simple_not_accepted', 'm_send_passkey_simple_pairing_confirm', 'm_send_passkey_simple_pairing_number', 'm_wait_passkey_simple_accepted', 'm_wait_passkey_simple_pairing_number', 'm_send_passkey_simple_accepted',
        'm_wait_passkey_failure_accepted', 'm_wait_oob_accepted', 'm_wait_oob_simple_pairing_number', 'm_send_oob_simple_accepted', 'm_wait_dhkey_accepted', 'm_wait_dhkey_dhkey_check', 'm_send_dhkey_accepted', 'm_wait_timing_timing_accuracy_res', 'm_send_version_res', 'm_wait_features_res',
        'm_send_features_features_res', 'm_wait_features_ext_res', 'm_send_features_ext_res', 'm_wait_switch_slot_offset', 'm_wait_switch_accepted', 'm_wait_hold_req_decision', 'm_send_hold_req_decision', 'm_wait_sniff_req_decision', 'm_send_sniff_req_decision', 'm_wait_unsniff_accepted',
        'm_wait_subrating_res', 'm_wait_sco_accepted', 'm_wait_sco_remove_accepted', 'm_wait_esco_accepted', 'm_send_esco_accepted', 'm_wait_remove_esco_accepted', 'm_send_remove_esco_accepted', 'm_wait_test_activate_accepted', 'm_wait_test_control_accepted', 'm_send_max_power', 
        'm_send_min_power', 'm_send_power_control_res', 'm_send_sam_type0_accepted_ext', 'm_send_sam_map_accepted_ext','m_send_sam_switch_accepted_ext', 'm_send_claimant_sres', 'm_send_responder_au_rand', 'm_send_pairing_accepted', 'm_send_fixed_accepted', 'm_send_creation_comb_key',
        'm_send_encryption_mode_accepted', 'm_send_io_capability_res', 'm_wait_resume_encryption_accepted', 'm_send_resume_encryption_start', 'm_wait_simple_res_pairing_number', 'm_send_simple_res_accepted', 'm_send_simple_res_pairing_number', 'm_wait_simple_res_accepted', 'm_wait_simple_dhkey_check',
        'm_send_simple_not_accepted', 'm_wait_passkey_simple_pairing_confirm', 'm_wait_passkey_res_simple_pairing_number', 'm_send_passkey_res_simple_accepted', 'm_send_passkey_res_simple_pairing_number', 'm_wait_passkey_res_simple_accepted', 'm_send_passkey_failure_accepted', 'm_send_oob_accepted',
        'm_send_oob_simple_pairing_number', 'm_wait_oob_simple_accepted', 'm_send_res_dhkey_accepted', 'm_send_dhkey_dhkey_check', 'm_wait_res_dhkey_accepted', 'm_send_timing_timing_accuracy_res', 'm_wait_switch_switch_req', 'm_send_switch_accepted',
        'm_send_res_hold_req_decision', 'm_wait_res_hold_req_decision', 'm_send_res_sniff_req_decision', 'm_wait_res_sniff_req_decision', 'm_send_subrating_res', 'm_send_res_sco_accepted', 'm_wait_res_sco_accepted', 'm_send_sco_remove_accepted', 'm_wait_esco_res_accepted', 'm_wait_res_esco_accepted',
        'm_send_res_esco_accepted',
        's_initial', 's_wait_version_res', 's_send_version_res', 's_send_switch_switch_req', 's_wait_switch_accepted', 's_wait_hold_hold', 's_wait_hold_req_decision', 's_send_hold_req_decision', 's_wait_sniff_req_decision', 's_send_sniff_req_decision', 's_wait_unsniff_accepted',
        's_wait_subrating_res', 's_wait_sco_accepted', 's_send_sco_accepted', 's_wait_sco_remove_accepted', 's_wait_esco_accepted', 's_send_esco_accepted', 's_wait_esco_initial_accepted', 's_wait_remove_esco_accepted', 's_send_remove_esco_accepted', 's_send_test_activate_accepted', 's_send_test_control_accepted',
        's_wait_max_power', 's_send_max_power', 's_wait_min_power', 's_send_min_power', 's_wait_power_control_res', 's_send_power_control_res', 's_wait_qos_accepted', 's_wait_page_accepted', 's_wait_page_scan_accepted', 's_wait_encapsulated_accepted', 's_wait_encapsulated_payload', 's_wait_payload_accepted',
        's_wait_ping_res', 's_send_clk_ack', 's_wait_sam_type0_accepted_ext', 's_send_sam_type0_accepted_ext', 's_wait_sam_map_accepted_ext', 's_send_sam_map_accepted_ext', 's_wait_sam_switch_accepted_ext', 's_send_sam_switch_accepted_ext', 's_wait_claimant_sres', 's_send_claimant_sres',
        's_wait_responder_au_rand', 's_send_responder_sres', 's_send_responder_au_rand', 's_wait_responder_sres', 's_wait_pairing_accepted', 's_send_pairing_accepted', 's_send_fixed_accepted', 's_wait_fixed_accepted', 's_wait_creation_comb_key', 's_send_creation_comb_key', 's_wait_temp_key', 
        's_send_semi_permanent_accepted', 's_wait_encryption_mode_accepted', 's_send_encryption_mode_accepted', 's_send_key_size_req_response', 's_wait_key_size_req_response', 's_send_start_encryption_accepted', 's_send_stop_encryption_accepted', 's_send_pause_encryption_pause_req',
        's_wait_pause_encryption_stop_encryption', 's_send_pause_encryption_accepted', 's_send_resume_encryption_accepted', 's_wait_key_size_mask_res', 's_send_io_capability_res', 's_wait_io_not_accepted_ext', 's_send_io_capability_col_res', 's_wait_io_capability_res', 's_send_simple_pairing_number',
        's_wait_simple_accepted', 's_wait_simple_pairing_number', 's_send_simple_accepted', 's_wait_simple_res_pairing_number', 's_send_simple_res_accepted', 's_send_simple_res_pairing_number', 's_wait_simple_res_accepted', 's_send_simple_dhkey_check', 's_wait_simple_not_accepted', 's_wait_simple_dhkey_check',
        's_send_simple_not_accepted', 's_wait_passkey_simple_pairing_confirm', 's_send_passkey_simple_pairing_number', 's_wait_passkey_simple_accepted', 's_wait_passkey_simple_pairing_number', 's_send_passkey_simple_accepted', 's_send_passkey_simple_pairing_confirm', 's_wait_passkey_res_simple_pairing_number',
        's_send_passkey_res_simple_accepted', 's_send_passkey_res_simple_pairing_number', 's_wait_passkey_res_simple_accepted', 's_wait_passkey_failure_accepted', 's_send_passkey_failure_accepted', 's_wait_oob_accepted', 's_wait_oob_simple_pairing_number', 's_send_oob_simple_accepted',
        's_send_oob_accepted', 's_send_oob_simple_pairing_number', 's_wait_oob_simple_accepted', 's_wait_dhkey_accepted', 's_wait_dhkey_dhkey_check', 's_send_dhkey_accepted', 's_send_res_dhkey_accepted', 's_send_dhkey_dhkey_check', 's_wait_res_dhkey_accepted', 's_wait_timing_timing_accuracy_res',
        's_send_timing_timing_accuracy_res', 's_send_clkoffset_res', 's_wait_features_res', 's_send_features_features_res', 's_wait_features_ext_res', 's_send_features_ext_res', 's_wait_name_res', 's_send_name_res', 's_send_switch_slot_offset', 's_send_switch_accepted',
        's_wait_hold_req_decision', 's_send_hold_req_decision', 's_send_res_hold_req_decision', 's_wait_res_hold_req_decision', 's_send_res_sniff_req_decision', 's_wait_res_sniff_req_decision', 's_send_unsniff_accepted', 's_send_subrating_res', 's_send_res_sco_accepted',
        's_send_sco_remove_accepted', 's_send_res_esco_accepted', 's_wait_res_esco_accepted'
]

transitions = [

    ### LMP_ACCEPTED
    {'trigger': 'recv_accepted', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_accepted', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_accepted', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'send_accepted', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_NOT_ACCEPTED
    {'trigger': 'recv_not_accepted', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_not_accepted', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_initial', 'dest': 's_initial'},

    # General not_accepted message
    {'trigger': 'recv_not_accepted', 'source': '*', 'dest': 'm_initial'},

##### Documentation ordered state transitions #####

    ### LMP_HOST_CONNECTION_REQ
    # 4.4.2: "the paging device always becomes the master of the piconet"
    {'trigger': 'send_host_connection_req', 'source': 'disconnected', 'dest': 'm_wait_host_connection_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_host_connection_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_host_connection_accepted', 'dest': 'disconnected'},

    {'trigger': 'recv_host_connection_req', 'source': 'disconnected', 'dest': 's_send_host_connection_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_host_connection_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_host_connection_accepted', 'dest': 'disconnected'},

    ### LMP_DETACH
    ## Closes connection.
    # Specification indicates that devices may send an LMP_DETACH PDU anytime
    {'trigger': 'send_detach', 'source': '*', 'dest': 'disconnected'},
    {'trigger': 'recv_detach', 'source': '*', 'dest': 'disconnected'},

    ### LMP_INCR_POWER_REQ
    ## Legacy power control
    {'trigger': 'send_incr_power_req', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_incr_power_req', 'source': 'm_initial', 'dest': 'm_wait_max_power'},
    {'trigger': 'recv_max_power', 'source': 'm_wait_max_power', 'dest': 'm_initial'},
    {'trigger': 'recv_incr_power_req', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_incr_power_req', 'source': 'm_initial', 'dest': 'm_send_max_power'},
    {'trigger': 'send_max_power', 'source': 'm_send_max_power', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_incr_power_req', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'send_incr_power_req', 'source': 's_initial', 'dest': 's_wait_max_power'},
    {'trigger': 'recv_max_power', 'source': 's_wait_max_power', 'dest': 's_initial'},
    {'trigger': 'recv_incr_power_req', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_incr_power_req', 'source': 's_initial', 'dest': 's_send_max_power'},
    {'trigger': 'send_max_power', 'source': 's_send_max_power', 'dest': 's_initial'},

    ### LMP_DECR_POWER_REQ
    ## Legacy power control
    # Decreasing power without problem. If no timeout is received then return to initial.
    # Decreasing power but the min power is reached
    {'trigger': 'send_decr_power_req', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_decr_power_req', 'source': 'm_initial', 'dest': 'm_wait_min_power'},
    {'trigger': 'recv_min_power', 'source': 'm_wait_min_power', 'dest': 'm_initial'},
    {'trigger': 'recv_decr_power_req', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_decr_power_req', 'source': 'm_initial', 'dest': 'm_send_min_power'},
    {'trigger': 'send_min_power', 'source': 'm_send_min_power', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_decr_power_req', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'send_decr_power_req', 'source': 's_initial', 'dest': 's_wait_min_power'},
    {'trigger': 'recv_min_power', 'source': 's_wait_min_power', 'dest': 's_initial'},
    {'trigger': 'recv_decr_power_req', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_decr_power_req', 'source': 's_initial', 'dest': 's_send_min_power'},
    {'trigger': 'send_min_power', 'source': 's_send_min_power', 'dest': 's_initial'},

    ### LMP_POWER_CONTROL_REQ
    ## Modern power control
    {'trigger': 'send_power_control_req', 'source': 'm_initial', 'dest': 'm_wait_power_control_res'},
    {'trigger': 'recv_power_control_res', 'source': 'm_wait_power_control_res', 'dest': 'm_initial'},
    {'trigger': 'recv_power_control_req', 'source': 'm_initial', 'dest': 'm_send_power_control_res'},
    {'trigger': 'send_power_control_res', 'source': 'm_send_power_control_res', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_power_control_req', 'source': 's_initial', 'dest': 's_wait_power_control_res'},
    {'trigger': 'recv_power_control_res', 'source': 's_wait_power_control_res', 'dest': 's_initial'},
    {'trigger': 'recv_power_control_req', 'source': 's_initial', 'dest': 's_send_power_control_res'},
    {'trigger': 'send_power_control_res', 'source': 's_send_power_control_res', 'dest': 's_initial'},


    ### LMP_SET_AFH
    ## Adaptive Frequency Hopping Control
    # This same PDU is used for the enabling, disabling and updating of AFH.
    # Configuration is by changing the AFH_mode parameter
    #
    # SPEC: The master shall not send a new LMP_SET_AFH PDU to a slave until it has
    # received the baseband acknowledgment for any previous LMP_SET_AFH
    # addressed to that slave and the instant has passed.
    {'trigger': 'send_set_afh', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_set_afh', 'source': 's_initial', 'dest': 's_initial'},
    # SM flags?

    #### LMP_CHANNEL_CLASSIFICATION_REQ
    ## Enables/disables channel classification reporting. Slave sends back LMP_CHANNEL_CLASSIFICATION PDUs indicating quality of channels.
    # May only be used when a slave is afh_reporting_mode = True.
    # Configuration is by changing the AFH_Reporting_Mode, AFH_Min_Interval, AFH_Max_Interval parameter
    {'trigger': 'send_channel_classification_req', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_channel_classification_req', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_CHANNEL_CLASSIFICATION
    # If slave's afh_reporting_mode = True then it shall generate these packets. Else it will not generate any channel classification reports.
    # Receives channel classification reporting. Slave sends back LMP_CHANNEL_CLASSIFICATION PDUs indicating quality of channels.
    # The sending of channel classification PDU by a slave should only occur after the master has enabled channel classification by sending
    # A classification request with the proper flags set
    {'trigger': 'recv_channel_classification', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_channel_classification', 'source': 's_initial', 'dest': 's_initial'},
    # SM flags?

    ### LMP_SUPERVISION_TIMEOUT
    ## Every physical link has a timer to determine that is used for link supervision.
    {'trigger': 'send_supervision_timeout', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_supervision_timeout', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_AUTO_RATE
    ## Packet to notify other side to use Channel Quality Driven Data Rate. 
    # Upon sending this, the other side can indicate which packet type they wish we use by sending a LMP_PREFERRED_RATE PDU.
    {'trigger': 'send_auto_rate', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_auto_rate', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_auto_rate', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_auto_rate', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_PREFERRED_RATE
    ## Only allowed to be sent after having received a LMP_AUTO_RATE packet in the past.
    {'trigger': 'send_preferred_rate', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_preferred_rate', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_preferred_rate', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_preferred_rate', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_QUALITY_OF_SERVICE
    # 
    {'trigger': 'send_quality_of_service', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_quality_of_service', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_QUALITY_OF_SERVICE_REQ
    # 
    {'trigger': 'send_quality_of_service_req', 'source': 'm_initial', 'dest': 'm_wait_qos_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_qos_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_qos_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_quality_of_service_req', 'source': 's_initial', 'dest': 's_wait_qos_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_qos_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_qos_accepted', 'dest': 's_initial'},

    ### LMP_PAGE_MODE_REQ
    # Procedure to negotiate the paging scheme used when we page another device.
    {'trigger': 'send_page_mode_req', 'source': 'm_initial', 'dest': 'm_wait_page_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_page_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_page_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_page_mode_req', 'source': 's_initial', 'dest': 's_wait_page_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_page_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_page_accepted', 'dest': 's_initial'},

    ### LMP_PAGE_SCAN_MODE_REQ
    # Procedure to negotiate the paging scheme used when another device pages us.
    {'trigger': 'send_page_scan_mode_req', 'source': 'm_initial', 'dest': 'm_wait_page_scan_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_page_scan_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_page_scan_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_page_scan_mode_req', 'source': 's_initial', 'dest': 's_wait_page_scan_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_page_scan_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_page_scan_accepted', 'dest': 's_initial'},

    ### LMP_MAX_SLOT
    # Informs the remote device of the maximum amount of slots that can be used.
    {'trigger': 'send_max_slot', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_max_slot', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'send_max_slot', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_max_slot', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_MAX_SLOT_REQ
    # Request a maximum amount of slots from a remote device, may be accepted or denied.
    {'trigger': 'send_max_slot_req', 'source': 'm_initial', 'dest': 'm_wait_slot_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_slot_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_slot_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_max_slot_req', 'source': 's_initial', 'dest': 's_wait_slot_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_slot_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_slot_accepted', 'dest': 's_initial'},

    ### LMP_PACKET_TYPE_TABLE_REQ
    # Part of using Enhanced Data Rate
    # Request change of packet type table on ACL logical transport.(packets and modulation mode)
    {'trigger': 'send_packet_type_table_req', 'source': 'm_initial', 'dest': 'm_wait_ptt_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_ptt_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_ptt_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_packet_type_table_req', 'source': 's_initial', 'dest': 's_wait_ptt_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_ptt_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_ptt_accepted', 'dest': 's_initial'},

    ### LMP_ENCAPSULATED_HEADER/PAYLOAD
    # Transaction used to send larger than regular amounts of data per packet.
    # In between the header and payloads and between the payloads either device should be able to send the following packets without a "different transaction collision"(HCI ERR) error:
    # LMP_CHANNEL_CLASSIFICATION, LMP_DECR_POWER_REQ, LMP_DETACH, LMP_INCR_POWER_REQ, LMP_MAX_POWER, LMP_MAX_SLOT, LMP_MIN_POWER, LMP_PREFERRED_RATE, LMP_SET_AFH
    {'trigger': 'send_encapsulated_header', 'source': 'm_initial', 'dest': 'm_wait_encapsulated_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_encapsulated_accepted', 'dest': 'm_wait_encapsulated_payload'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_encapsulated_accepted', 'dest': 'm_initial'},

    {'trigger': 'recv_encapsulated_payload', 'source': 'm_wait_encapsulated_payload', 'dest': 'm_wait_payload_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_payload_accepted', 'dest': 'm_wait_encapsulated_payload'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_payload_accepted', 'dest': 'm_wait_encapsulated_payload'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_payload_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_payload_accepted', 'dest': 'm_initial'},

    {'trigger': 'send_encapsulated_header', 'source': 's_initial', 'dest': 's_wait_encapsulated_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_encapsulated_accepted', 'dest': 's_wait_encapsulated_payload'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_encapsulated_accepted', 'dest': 's_initial'},

    {'trigger': 'recv_encapsulated_payload', 'source': 's_wait_encapsulated_payload', 'dest': 's_wait_payload_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_payload_accepted', 'dest': 's_wait_encapsulated_payload'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_payload_accepted', 'dest': 's_wait_encapsulated_payload'},
    {'trigger': 'recv_accepted', 'source': 's_wait_payload_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_payload_accepted', 'dest': 's_initial'},

    ### LMP_PING_REQ/RES
    # Verify the presence of the remote Link Manager and optionally verify message integrity
    # When both devices support this feature only -> Need to process LMP_FEATURES_RES(_EXT) first to verify that it it supported.
    {'trigger': 'send_ping_req', 'source': 'm_initial', 'dest': 'm_wait_ping_res'},
    {'trigger': 'recv_ping_res', 'source': 'm_wait_ping_res', 'dest': 'm_initial'},
    {'trigger': 'send_ping_req', 'source': 's_initial', 'dest': 's_wait_ping_res'},
    {'trigger': 'recv_ping_res', 'source': 's_wait_ping_res', 'dest': 's_initial'},

    ### LMP_CLK_ADJ/ACK
    # Adjusting piconet clock
    {'trigger': 'send_clk_adj', 'source': 'm_initial', 'dest': 'm_wait_clk_ack'},
    {'trigger': 'recv_clk_adj_ack', 'source': 'm_wait_clk_ack', 'dest': 'm_initial'},
    {'trigger': 'recv_clk_adj', 'source': 's_initial', 'dest': 's_send_clk_ack'},
    {'trigger': 'send_clk_adj_ack', 'source': 's_send_clk_ack', 'dest': 's_initial'},

    ### LMP_CLK_ADJ_REQ
    # Slave requests clk adjustment
    {'trigger': 'recv_clk_adj_req', 'source': 'm_initial', 'dest': 'm_send_clk_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_clk_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_clk_accepted_ext', 'dest': 'm_initial'},

    {'trigger': 'send_clk_adj_req', 'source': 's_initial', 'dest': 's_wait_clk_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_clk_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_clk_accepted_ext', 'dest': 's_initial'},

    ### LMP_SAM_SET_TYPE0
    # Slot availability Mask
    {'trigger': 'send_sam_set_typ0', 'source': 'm_initial', 'dest': 'm_wait_sam_type0_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_sam_type0_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_sam_type0_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'recv_sam_set_typ0', 'source': 'm_initial', 'dest': 'm_send_sam_type0_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_sam_type0_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_sam_type0_accepted_ext', 'dest': 'm_initial'},
    
    {'trigger': 'send_sam_set_typ0', 'source': 's_initial', 'dest': 's_wait_sam_type0_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_sam_type0_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_sam_type0_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_sam_set_typ0', 'source': 's_initial', 'dest': 's_send_sam_type0_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_sam_type0_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 's_send_sam_type0_accepted_ext', 'dest': 's_initial'},

    ### LMP_SAM_DEFINE_MAP
    {'trigger': 'send_sam_define_map', 'source': 'm_initial', 'dest': 'm_wait_sam_map_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_sam_map_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_sam_map_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'recv_sam_define_map', 'source': 'm_initial', 'dest': 'm_send_sam_map_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_sam_map_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_sam_map_accepted_ext', 'dest': 'm_initial'},

    {'trigger': 'send_sam_define_map', 'source': 's_initial', 'dest': 's_wait_sam_map_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_sam_map_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_sam_map_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_sam_define_map', 'source': 's_initial', 'dest': 's_send_sam_map_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_sam_map_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 's_send_sam_map_accepted_ext', 'dest': 's_initial'},

    ### LMP_SAM_SWITCH
    {'trigger': 'send_sam_switch', 'source': 'm_initial', 'dest': 'm_wait_sam_switch_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_sam_switch_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_sam_switch_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'recv_sam_switch', 'source': 'm_initial', 'dest': 'm_send_sam_switch_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_sam_switch_accepted_ext', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_sam_switch_accepted_ext', 'dest': 'm_initial'},

    {'trigger': 'send_sam_switch', 'source': 's_initial', 'dest': 's_wait_sam_switch_accepted_ext'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_sam_switch_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_sam_switch_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'recv_sam_switch', 'source': 's_initial', 'dest': 's_send_sam_switch_accepted_ext'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_sam_switch_accepted_ext', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 's_send_sam_switch_accepted_ext', 'dest': 's_initial'},


####  Security 4.2 p619
    ### LMP_AU_RAND & SRES
    # sres: Claimant has link key (legacy authentication)
    # not_accepted: Claimant has no link key (legacy and secure authentication)
    # When the authentication attempt fails an exponentially increasing waiting interval to a implementation dependent maximum.
    # Private key should be new with every repeated attempt to prevent leaking info
    {'trigger': 'send_au_rand', 'source': 'm_initial', 'dest': 'm_wait_claimant_sres'},
    {'trigger': 'recv_sres', 'source': 'm_wait_claimant_sres', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_claimant_sres', 'dest': 'm_initial'},
    {'trigger': 'recv_au_rand', 'source': 'm_initial', 'dest': 'm_send_claimant_sres'},
    {'trigger': 'send_sres', 'source': 'm_send_claimant_sres', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_claimant_sres', 'dest': 'm_initial'},

    {'trigger': 'send_au_rand', 'source': 's_initial', 'dest': 's_wait_claimant_sres'},
    {'trigger': 'recv_sres', 'source': 's_wait_claimant_sres', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_claimant_sres', 'dest': 's_initial'},
    {'trigger': 'recv_au_rand', 'source': 's_initial', 'dest': 's_send_claimant_sres'},
    {'trigger': 'send_sres', 'source': 's_send_claimant_sres', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_claimant_sres', 'dest': 's_initial'},

    ## Responder has link key (secure authentication)
    # Master: Initiating Master
    {'trigger': 'send_au_rand', 'source': 'm_initial', 'dest': 'm_wait_responder_au_rand'},
    {'trigger': 'recv_au_rand', 'source': 'm_wait_responder_au_rand', 'dest': 'm_wait_responder_sres'},
    # Master: Initiating Slave
    {'trigger': 'recv_au_rand', 'source': 'm_initial', 'dest': 'm_send_responder_au_rand'},
    {'trigger': 'send_au_rand', 'source': 'm_send_responder_au_rand', 'dest': 'm_wait_responder_sres'},
    # LMP_SRES
    {'trigger': 'recv_sres', 'source': 'm_wait_responder_sres', 'dest': 'm_send_responder_sres'},
    {'trigger': 'send_sres', 'source': 'm_send_responder_sres', 'dest': 'm_initial'},

    # Slave: Initiating Slave
    {'trigger': 'send_au_rand', 'source': 's_initial', 'dest': 's_wait_responder_au_rand'},
    {'trigger': 'recv_au_rand', 'source': 's_wait_responder_au_rand', 'dest': 's_send_responder_sres'},
    # Slave: Initiating Master
    {'trigger': 'recv_au_rand', 'source': 's_initial', 'dest': 's_send_responder_au_rand'},
    {'trigger': 'send_au_rand', 'source': 's_send_responder_au_rand', 'dest': 's_wait_responder_sres'},
    # LMP_SRES
    {'trigger': 'send_sres', 'source': 's_send_responder_sres', 'dest': 's_wait_responder_sres'},
    {'trigger': 'recv_sres', 'source': 's_wait_responder_sres', 'dest': 's_initial'},

#### PAIRING
# Page 623

    ### LMP_IN_RAND
    ## Initiating Master: Responder accepts/rejects pairing
    {'trigger': 'send_in_rand', 'source': 'm_initial', 'dest': 'm_wait_pairing_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_pairing_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_pairing_accepted', 'dest': 'm_initial'},
    # Responding Master
    {'trigger': 'recv_in_rand', 'source': 'm_initial', 'dest': 'm_send_pairing_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_pairing_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_pairing_accepted', 'dest': 'm_initial'},

    ## Initiating Slave: Responder accepts/rejects pairing
    {'trigger': 'send_in_rand', 'source': 's_initial', 'dest': 's_wait_pairing_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_pairing_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_pairing_accepted', 'dest': 's_initial'},
    # Responding Slave
    {'trigger': 'recv_in_rand', 'source': 's_initial', 'dest': 's_send_pairing_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_pairing_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_pairing_accepted', 'dest': 's_initial'},

    ## Initiating Master: Responder has fixed pin
    {'trigger': 'recv_in_rand', 'source': 'm_wait_pairing_accepted', 'dest': 'm_send_fixed_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_fixed_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_fixed_accepted', 'dest': 'm_initial'},
    # Responding Master: Responder has fixed pin
    {'trigger': 'send_in_rand', 'source': 'm_send_pairing_accepted', 'dest': 'm_wait_fixed_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_fixed_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_fixed_accepted', 'dest': 'm_initial'},

    ## Initiating Slave: Responder has fixed pin
    {'trigger': 'recv_in_rand', 'source': 's_wait_pairing_accepted', 'dest': 's_send_fixed_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_fixed_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_fixed_accepted', 'dest': 's_initial'},
    # Responding Slave: Responder has fixed pin
    {'trigger': 'send_in_rand', 'source': 's_send_pairing_accepted', 'dest': 's_wait_fixed_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_fixed_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_fixed_accepted', 'dest': 's_initial'},

#### Change link key
    ### LMP_COMB_KEY & LMP_UNIT_KEY
    # Link key creation and changing
    {'trigger': 'send_comb_key', 'source': 'm_initial', 'dest': 'm_wait_creation_comb_key'},
    {'trigger': 'recv_comb_key', 'source': 'm_wait_creation_comb_key', 'dest': 'm_initial'},
    {'trigger': 'recv_comb_key', 'source': 'm_initial', 'dest': 'm_send_creation_comb_key'},
    {'trigger': 'send_comb_key', 'source': 'm_send_creation_comb_key', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_comb_key', 'source': 's_initial', 'dest': 's_wait_creation_comb_key'},
    {'trigger': 'recv_comb_key', 'source': 's_wait_creation_comb_key', 'dest': 's_initial'},
    {'trigger': 'recv_comb_key', 'source': 's_initial', 'dest': 's_send_creation_comb_key'},
    {'trigger': 'send_comb_key', 'source': 's_send_creation_comb_key', 'dest': 's_initial'},
    
    ### LMP_TEMP_RAND & LMP_TEMP_KEY
    # Change to a temporary link key
    {'trigger': 'send_temp_rand', 'source': 'm_initial', 'dest': 'm_send_temp_key'},
    {'trigger': 'send_temp_key', 'source': 'm_send_temp_key', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_temp_rand', 'source': 's_initial', 'dest': 's_wait_temp_key'},
    {'trigger': 'recv_temp_key', 'source': 's_wait_temp_key', 'dest': 's_initial'},


    ### LMP_USE_SEMI_PERMANENT_KEY
    # Change to a semi-permanent link key
    {'trigger': 'send_use_semi_permanent_key', 'source': 'm_initial', 'dest': 'm_wait_semi_permanent_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_semi_permanent_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_use_semi_permanent_key', 'source': 's_initial', 'dest': 's_send_semi_permanent_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_semi_permanent_accepted', 'dest': 's_initial'},

    ### LMP_ENCRYPTION_MODE_REQ
    # Initiating master
    {'trigger': 'send_encryption_mode_req', 'source': 'm_initial', 'dest': 'm_wait_encryption_mode_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_encryption_mode_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_encryption_mode_accepted', 'dest': 'm_initial'},
    # Responding master
    {'trigger': 'recv_encryption_mode_req', 'source': 'm_initial', 'dest': 'm_send_encryption_mode_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_encryption_mode_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_encryption_mode_accepted', 'dest': 'm_initial'},

    # Initiating Slave
    {'trigger': 'send_encryption_mode_req', 'source': 's_initial', 'dest': 's_wait_encryption_mode_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_encryption_mode_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_encryption_mode_accepted', 'dest': 's_initial'},
    # Responding Slave
    {'trigger': 'recv_encryption_mode_req', 'source': 's_initial', 'dest': 's_send_encryption_mode_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_encryption_mode_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_encryption_mode_accepted', 'dest': 's_initial'},

    ### LMP_ENCRYPTION_KEY_SIZE_REQ
    # Encryption key size req
    {'trigger': 'send_encryption_key_size_req', 'source': 'm_initial', 'dest': 'm_wait_key_size_req_response'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_key_size_req_response', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_key_size_req_response', 'dest': 'm_initial'},
    {'trigger': 'recv_encryption_key_size_req', 'source': 'm_wait_key_size_req_response', 'dest': 'm_send_key_size_req_response'},

    {'trigger': 'send_encryption_key_size_req', 'source': 'm_send_key_size_req_response', 'dest': 'm_wait_key_size_req_response'},
    {'trigger': 'send_accepted', 'source': 'm_send_key_size_req_response', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_key_size_req_response', 'dest': 'm_initial'},

    # Slave
    {'trigger': 'recv_encryption_key_size_req', 'source': 's_initial', 'dest': 's_send_key_size_req_response'},
    {'trigger': 'send_accepted', 'source': 's_send_key_size_req_response', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_key_size_req_response', 'dest': 's_initial'},
    {'trigger': 'send_encryption_key_size_req', 'source': 's_send_key_size_req_response', 'dest': 's_wait_key_size_req_response'},

    {'trigger': 'recv_encryption_key_size_req', 'source': 's_wait_key_size_req_response', 'dest': 's_send_key_size_req_response'},
    {'trigger': 'recv_accepted', 'source': 's_wait_key_size_req_response', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_key_size_req_response', 'dest': 's_initial'},

    ### LMP_START_ENCRYPTION_REQ
    # Start Encryption
    {'trigger': 'send_start_encryption_req', 'source': 'm_initial', 'dest': 'm_wait_start_encryption_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_start_encryption_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_start_encryption_req', 'source': 's_initial', 'dest': 's_send_start_encryption_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_start_encryption_accepted', 'dest': 's_initial'},

    ### LMP_STOP_ENCRYPTION_REQ
    # Stop Encryption
    {'trigger': 'send_stop_encryption_req', 'source': 'm_initial', 'dest': 'm_wait_stop_encryption_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_stop_encryption_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_stop_encryption_req', 'source': 's_initial', 'dest': 's_send_stop_encryption_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_stop_encryption_accepted', 'dest': 's_initial'},

    ### LMP_PAUSE_ENCRYPTION_REQ
    # Stop Encryption
    {'trigger': 'send_pause_encryption_req', 'source': 'm_initial', 'dest': 'm_wait_pause_encryption_pause_req'},
    {'trigger': 'recv_pause_encryption_req', 'source': 'm_wait_pause_encryption_pause_req', 'dest': 'm_send_pause_encryption_stop_encryption'},
    {'trigger': 'send_stop_encryption', 'source': 'm_send_pause_encryption_stop_encryption', 'dest': 'm_wait_pause_encryption_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_pause_encryption_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_pause_encryption_req', 'source': 's_initial', 'dest': 's_send_pause_encryption_pause_req'},
    {'trigger': 'send_pause_encryption_req', 'source': 's_send_pause_encryption_pause_req', 'dest': 's_wait_pause_encryption_stop_encryption'},
    {'trigger': 'recv_stop_encryption', 'source': 's_wait_pause_encryption_stop_encryption', 'dest': 's_send_pause_encryption_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_pause_encryption_accepted', 'dest': 's_initial'},

    ### LMP_PAUSE_ENCRYPTION_AES_REQ
    # Pause AES encryption
    {'trigger': 'send_pause_encryption_aes_req', 'source': 'm_initial', 'dest': 'm_wait_pause_encryption_pause_req'},
    # Slave reception
    {'trigger': 'recv_pause_encryption_aes_req', 'source': 's_initial', 'dest': 's_send_pause_encryption_pause_req'},
    ## Slave initiated: Slave side
    # SPECIFICATION INDICATES THE FOLLOWING BUT IT LOOKS WRONG TO ME
    {'trigger': 'send_pause_encryption_req', 'source': 's_initial', 'dest': 's_wait_pause_encryption_stop_encryption'},
    # Master side
    {'trigger': 'recv_pause_encryption_req', 'source': 'm_initial', 'dest': 'm_send_pause_encryption_stop_encryption'},

    ### LMP_RESUME_ENCRYPTION_REQ
    # Master initiated: Master side
    {'trigger': 'send_start_encryption', 'source': 'm_initial', 'dest': 'm_wait_resume_encryption_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_resume_encryption_accepted', 'dest': 'm_initial'},
    # Master initiated: Slave side
    {'trigger': 'recv_start_encryption', 'source': 's_initial', 'dest': 's_send_resume_encryption_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_resume_encryption_accepted', 'dest': 's_initial'},

    # Slave initiated: Slave side
    {'trigger': 'send_resume_encryption_req', 'source': 's_initial', 'dest': 's_wait_resume_encryption_start'},
    {'trigger': 'recv_start_encryption', 'source': 's_wait_resume_encryption_start', 'dest': 's_send_resume_encryption_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_resume_encryption_accepted', 'dest': 's_initial'},
    # Slave initiated: Master side
    {'trigger': 'recv_resume_encryption_req', 'source': 'm_initial', 'dest': 'm_send_resume_encryption_start'},
    {'trigger': 'send_start_encryption', 'source': 'm_send_resume_encryption_start', 'dest': 'm_wait_resume_encryption_accepted'},

    ### LMP_ENCRYPTION_KEY_SIZE_MASK_REQ
    # Stop Encryption
    {'trigger': 'send_encryption_key_size_mask_req', 'source': 'm_initial', 'dest': 'm_wait_key_size_mask_res'},
    {'trigger': 'recv_encryption_key_size_mask_res', 'source': 'm_wait_key_size_mask_res', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_encryption_key_size_mask_req', 'source': 's_initial', 'dest': 's_wait_key_size_mask_res'},
    {'trigger': 'send_encryption_key_size_mask_res', 'source': 's_wait_key_size_mask_res', 'dest': 's_initial'},

#### SECURE SIMPLE PAIRING ####
## - IO Capability REQ: Which algorithm do we use for authentication stage 1?
## - Public key exchange
## - Authentication stage 1. Algorithm to use is decided by: see bottom p.642

    ### LMP_IO_CAPABILITY_REQ
    # IO capabilities exchange. Should resolve the authentication stage 1 to use 1 of:
    # - Numeric comparison
    # - Passkey entry
    # - Out of band
    ## Master initiating: Master side
    {'trigger': 'send_io_capability_req', 'source': 'm_initial', 'dest': 'm_wait_io_capability_res'},
    {'trigger': 'recv_io_capability_res', 'source': 'm_wait_io_capability_res', 'dest': 'm_initial'},
    # Collision handling
    {'trigger': 'recv_io_capability_req', 'source': 'm_wait_io_capability_res', 'dest': 'm_send_io_not_accepted_ext'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_io_not_accepted_ext', 'dest': 'm_wait_io_capability_col_res'},
    {'trigger': 'recv_io_capability_res', 'source': 'm_wait_io_capability_col_res', 'dest': 'm_initial'},
    ## Master initiating: Slave side
    {'trigger': 'recv_io_capability_req', 'source': 's_initial', 'dest': 's_send_io_capability_res'},
    {'trigger': 'send_io_capability_res', 'source': 's_send_io_capability_res', 'dest': 's_initial'},
    # Collision handling
    {'trigger': 'send_io_capability_req', 'source': 's_send_io_capability_res', 'dest': 's_wait_io_not_accepted_ext'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_io_not_accepted_ext', 'dest': 's_send_io_capability_col_res'},
    {'trigger': 'send_io_capability_res', 'source': 's_send_io_capability_col_res', 'dest': 'm_initial'},

    ## Slave initiating: Slave side
    {'trigger': 'send_io_capability_req', 'source': 's_initial', 'dest': 's_wait_io_capability_res'},
    {'trigger': 'recv_io_capability_res', 'source': 's_wait_io_capability_res', 'dest': 's_initial'},
    # Collision handling
    {'trigger': 'recv_io_capability_req', 'source': 's_wait_io_capability_res', 'dest': 's_wait_io_not_accepted_ext'},

    ## Slave initiating: Master side
    {'trigger': 'recv_io_capability_req', 'source': 'm_initial', 'dest': 'm_send_io_capability_res'},
    {'trigger': 'send_io_capability_res', 'source': 'm_send_io_capability_res', 'dest': 'm_initial'},
    # Collision handling
    {'trigger': 'send_io_capability_req', 'source': 'm_send_io_capability_res', 'dest': 'm_send_io_not_accepted_ext'},

    ### LMP_ENCAPSULATED_HEADER
    # Public key exchange
    # This uses the encapsulated payload
    # LMP_ENCAPSULATED_HEADER -> : <- LMP_ACCEPTED
    # LMP_ENCAPSULATED_PAYLOAD -> : <- LMP_ACCEPTED (N TIMES)
    # LMP_ENCAPSULATED_HEADER -> : <- LMP_ACCEPTED
    # LMP_ENCAPSULATED_PAYLOAD -> : <- LMP_ACCEPTED (N TIMES)

    ### LMP_SIMPLE_PAIRING_CONFIRM, LMP_SIMPLE_PAIRING_NUMBER
    # Triggered after Public key exchange
    # Authentication stage 1
    # Initiating Master
    {'trigger': 'recv_simple_pairing_confirm', 'source': 'm_initial', 'dest': 'm_send_simple_pairing_number'},
    {'trigger': 'send_simple_pairing_number', 'source': 'm_send_simple_pairing_number', 'dest': 'm_wait_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_simple_accepted', 'dest': 'm_wait_simple_pairing_number'},
    {'trigger': 'recv_simple_pairing_number', 'source': 'm_wait_simple_pairing_number', 'dest': 'm_send_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_simple_accepted', 'dest': 'm_initial'},
    # Responding Master
    {'trigger': 'send_simple_pairing_confirm', 'source': 'm_initial', 'dest': 'm_wait_simple_res_pairing_number'},
    {'trigger': 'recv_simple_pairing_number', 'source': 'm_wait_simple_res_pairing_number', 'dest': 'm_send_simple_res_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_simple_res_accepted', 'dest': 'm_send_simple_res_pairing_number'},
    {'trigger': 'send_simple_pairing_number', 'source': 'm_send_simple_res_pairing_number', 'dest': 'm_wait_simple_res_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_simple_res_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_simple_res_accepted', 'dest': 'm_initial'},

    # Initiating Slave
    {'trigger': 'recv_simple_pairing_confirm', 'source': 's_initial', 'dest': 's_send_simple_pairing_number'},
    {'trigger': 'send_simple_pairing_number', 'source': 's_send_simple_pairing_number', 'dest': 's_wait_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_simple_accepted', 'dest': 's_wait_simple_pairing_number'},
    {'trigger': 'recv_simple_pairing_number', 'source': 's_wait_simple_pairing_number', 'dest': 's_send_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_simple_accepted', 'dest': 's_initial'},
    # Responding Slave
    {'trigger': 'send_simple_pairing_confirm', 'source': 's_initial', 'dest': 's_wait_simple_res_pairing_number'},
    {'trigger': 'recv_simple_pairing_number', 'source': 's_wait_simple_res_pairing_number', 'dest': 's_send_simple_res_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_simple_res_accepted', 'dest': 's_send_simple_res_pairing_number'},
    {'trigger': 'send_simple_pairing_number', 'source': 's_send_simple_res_pairing_number', 'dest': 's_wait_simple_res_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_simple_res_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_simple_res_accepted', 'dest': 's_initial'},

    ### LMP_NUMERIC_COMPARISON_FAILED
    # If the initiating side notices that the confirm values do not match the initiating LM shall send LMP_NUMERIC_FAILED
    # If the responding side notices that the confirm values do not match this is only communicated after the LMP_DHKEY_CHECK
    {'trigger': 'send_numeric_comparison_failed', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_numeric_comparison_failed', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_numeric_comparison_failed', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_numeric_comparison_failed', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_DHKEY_CHECK
    # Master initiating
    {'trigger': 'send_accepted', 'source': 'm_send_simple_accepted', 'dest': 'm_send_simple_dhkey_check'},
    {'trigger': 'send_dhkey_check', 'source': 'm_send_simple_dhkey_check', 'dest': 'm_wait_simple_not_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_simple_not_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_accepted', 'source': 'm_wait_simple_res_accepted', 'dest': 'm_wait_simple_dhkey_check'},
    {'trigger': 'recv_dhkey_check', 'source': 'm_wait_simple_dhkey_check', 'dest': 'm_send_simple_not_accepted'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_simple_not_accepted', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_accepted', 'source': 's_send_simple_accepted', 'dest': 's_send_simple_dhkey_check'},
    {'trigger': 'send_dhkey_check', 'source': 's_send_simple_dhkey_check', 'dest': 's_wait_simple_not_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_simple_not_accepted', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_accepted', 'source': 's_wait_simple_res_accepted', 'dest': 's_wait_simple_dhkey_check'},
    {'trigger': 'recv_dhkey_check', 'source': 's_wait_simple_dhkey_check', 'dest': 's_send_simple_not_accepted'},
    {'trigger': 'send_not_accepted', 'source': 's_send_simple_not_accepted', 'dest': 's_initial'},

    ### Authentication stage 1: Passkey Entry Authentication
    # After receiving the passkey reply -> IO capability request has resolved in Passkey entry authentication
    # Uses the LMP_SIMPLE_PAIRING_CONFIRM, LMP_SIMPLE_PAIRING_NUMBER transaction 20 times
    # Master initiating
    {'trigger': 'send_simple_pairing_confirm', 'source': 'm_initial', 'dest': 'm_wait_passkey_simple_pairing_confirm'},
    {'trigger': 'recv_simple_pairing_confirm', 'source': 'm_wait_passkey_simple_pairing_confirm', 'dest': 'm_send_passkey_simple_pairing_number'},
    {'trigger': 'send_simple_pairing_number', 'source': 'm_send_passkey_simple_pairing_number', 'dest': 'm_wait_passkey_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_passkey_simple_accepted', 'dest': 'm_wait_passkey_simple_pairing_number'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_passkey_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_simple_pairing_number', 'source': 'm_wait_passkey_simple_pairing_number', 'dest': 'm_send_passkey_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_passkey_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_passkey_simple_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_simple_pairing_confirm', 'source': 'm_initial', 'dest': 'm_send_passkey_simple_pairing_confirm'},
    {'trigger': 'send_simple_pairing_confirm', 'source': 'm_send_passkey_simple_pairing_confirm', 'dest': 'm_wait_passkey_res_simple_pairing_number'},
    {'trigger': 'recv_simple_pairing_number', 'source': 'm_wait_passkey_res_simple_pairing_number', 'dest': 'm_send_passkey_res_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_passkey_res_simple_accepted', 'dest': 'm_send_passkey_res_simple_pairing_number'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_passkey_res_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_simple_pairing_number', 'source': 'm_send_passkey_res_simple_pairing_number', 'dest': 'm_wait_passkey_res_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_passkey_res_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_passkey_res_simple_accepted', 'dest': 'm_initial'},

    # Slave initiating
    {'trigger': 'send_simple_pairing_confirm', 'source': 's_initial', 'dest': 's_wait_passkey_simple_pairing_confirm'},
    {'trigger': 'recv_simple_pairing_confirm', 'source': 's_wait_passkey_simple_pairing_confirm', 'dest': 's_send_passkey_simple_pairing_number'},
    {'trigger': 'send_simple_pairing_number', 'source': 's_send_passkey_simple_pairing_number', 'dest': 's_wait_passkey_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_passkey_simple_accepted', 'dest': 's_wait_passkey_simple_pairing_number'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_passkey_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_simple_pairing_number', 'source': 's_wait_passkey_simple_pairing_number', 'dest': 's_send_passkey_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_passkey_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_passkey_simple_accepted', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_simple_pairing_confirm', 'source': 's_initial', 'dest': 's_send_passkey_simple_pairing_confirm'},
    {'trigger': 'send_simple_pairing_confirm', 'source': 's_send_passkey_simple_pairing_confirm', 'dest': 's_wait_passkey_res_simple_pairing_number'},
    {'trigger': 'recv_simple_pairing_number', 'source': 's_wait_passkey_res_simple_pairing_number', 'dest': 's_send_passkey_res_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_passkey_res_simple_accepted', 'dest': 's_send_passkey_res_simple_pairing_number'},
    {'trigger': 'send_not_accepted', 'source': 's_send_passkey_res_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'send_simple_pairing_number', 'source': 's_send_passkey_res_simple_pairing_number', 'dest': 's_wait_passkey_res_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_passkey_res_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_passkey_res_simple_accepted', 'dest': 's_initial'},

    ### LMP_PASSKEY_ENTRY_FAILED
    # Passkey Failure on initiating
    {'trigger': 'send_passkey_entry_failed', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_passkey_entry_failed', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_passkey_entry_failed', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_passkey_entry_failed', 'source': 's_initial', 'dest': 's_initial'},

    ## Passkey Failure on responding
    # Master
    {'trigger': 'send_simple_pairing_confirm', 'source': 'm_initial', 'dest': 'm_wait_passkey_failure_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_passkey_failure_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_simple_pairing_confirm', 'source': 'm_initial', 'dest': 'm_send_passkey_failure_accepted'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_passkey_failure_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_simple_pairing_confirm', 'source': 's_initial', 'dest': 's_wait_passkey_failure_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_passkey_failure_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_simple_pairing_confirm', 'source': 's_initial', 'dest': 's_send_passkey_failure_accepted'},
    {'trigger': 'send_not_accepted', 'source': 's_send_passkey_failure_accepted', 'dest': 's_initial'},

    ### LMP_KEYPRESS_NOTIFICATION 
    # Keypress notifications
    # When the host sets the IO capabilities to KeyboardOnly IO and SSP is supported on the host and controller
    {'trigger': 'send_keypress_notification', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_keypress_notification', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_keypress_notification', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_keypress_notification', 'source': 's_initial', 'dest': 's_initial'},

    ### Authentication stage 1: OOB
    # Uses an Out Of Band protocol to facilitate authentication
    # Master Initiating
    {'trigger': 'send_simple_pairing_number', 'source': 'm_initial', 'dest': 'm_wait_oob_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_oob_accepted', 'dest': 'm_wait_oob_simple_pairing_number'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_oob_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_simple_pairing_number', 'source': 'm_wait_oob_simple_pairing_number', 'dest': 'm_send_oob_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_oob_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_oob_simple_accepted', 'dest': 'm_initial'},
    # Master Responding
    {'trigger': 'recv_simple_pairing_number', 'source': 'm_initial', 'dest': 'm_send_oob_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_oob_accepted', 'dest': 'm_send_oob_simple_pairing_number'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_oob_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_simple_pairing_number', 'source': 'm_send_oob_simple_pairing_number', 'dest': 'm_wait_oob_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_oob_simple_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_oob_simple_accepted', 'dest': 'm_initial'},
    # Slave Initiating
    {'trigger': 'send_simple_pairing_number', 'source': 's_initial', 'dest': 's_wait_oob_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_oob_accepted', 'dest': 's_wait_oob_simple_pairing_number'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_oob_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_simple_pairing_number', 'source': 's_wait_oob_simple_pairing_number', 'dest': 's_send_oob_simple_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_oob_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_oob_simple_accepted', 'dest': 's_initial'},
    # Slave Responding
    {'trigger': 'recv_simple_pairing_number', 'source': 's_initial', 'dest': 's_send_oob_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_oob_accepted', 'dest': 's_send_oob_simple_pairing_number'},
    {'trigger': 'send_not_accepted', 'source': 's_send_oob_accepted', 'dest': 's_initial'},
    {'trigger': 'send_simple_pairing_number', 'source': 's_send_oob_simple_pairing_number', 'dest': 's_wait_oob_simple_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_oob_simple_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_oob_simple_accepted', 'dest': 's_initial'},

    ### LMP_OOB_FAILED
    # Out of band information not available on the initiator side
    {'trigger': 'send_oob_failed', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_oob_failed', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_oob_failed', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_oob_failed', 'source': 's_initial', 'dest': 's_initial'},

    ### Authentication stage 2: DHKey check

    ### LMP_DHKEY_CHECK
    # Master initiating
    {'trigger': 'send_dhkey_check', 'source': 'm_initial', 'dest': 'm_wait_dhkey_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_dhkey_accepted', 'dest': 'm_wait_dhkey_dhkey_check'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_dhkey_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_dhkey_check', 'source': 'm_wait_dhkey_dhkey_check', 'dest': 'm_send_dhkey_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_dhkey_accepted', 'dest': 'm_initial'},
    # Documentation error: text indicates the following transition, but the diagram does not.
    # {'trigger': 'send_not_accepted', 'source': 'm_send_dhkey_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_dhkey_check', 'source': 'm_initial', 'dest': 'm_send_res_dhkey_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_res_dhkey_accepted', 'dest': 'm_send_dhkey_dhkey_check'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_res_dhkey_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_dhkey_check', 'source': 'm_send_dhkey_dhkey_check', 'dest': 'm_wait_res_dhkey_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_res_dhkey_accepted', 'dest': 'm_initial'},
    # Documentation error: text indicates the following transition, but the diagram does not.
    # {'trigger': 'recv_not_accepted', 'source': 'm_wait_res_dhkey_accepted', 'dest': 'm_initial'},

    # Slave initiating
    {'trigger': 'send_dhkey_check', 'source': 's_initial', 'dest': 's_wait_dhkey_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_dhkey_accepted', 'dest': 's_wait_dhkey_dhkey_check'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_dhkey_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_dhkey_check', 'source': 's_wait_dhkey_dhkey_check', 'dest': 's_send_dhkey_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_dhkey_accepted', 'dest': 's_initial'},
    # Documentation error: text indicates the following transition, but the diagram does not.
    # {'trigger': 'send_not_accepted', 'source': 's_send_dhkey_accepted', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_dhkey_check', 'source': 's_initial', 'dest': 's_send_res_dhkey_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_res_dhkey_accepted', 'dest': 's_send_dhkey_dhkey_check'},
    {'trigger': 'send_not_accepted', 'source': 's_send_res_dhkey_accepted', 'dest': 's_initial'},
    {'trigger': 'send_dhkey_check', 'source': 's_send_dhkey_dhkey_check', 'dest': 's_wait_res_dhkey_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_res_dhkey_accepted', 'dest': 's_initial'},
    # Documentation error: text indicates the following transition, but the diagram does not.
    # {'trigger': 'recv_not_accepted', 'source': 's_wait_res_dhkey_accepted', 'dest': 's_initial'},

#### INFORMATIONAL REQUESTS ####
    
    ### LMP_TIMING_ACCURACY_REQ & LMP_TIMING_ACCURACY_RES
    # Master initiating
    {'trigger': 'send_timing_accuracy_req', 'source': 'm_initial', 'dest': 'm_wait_timing_timing_accuracy_res'},
    {'trigger': 'recv_timing_accuracy_res', 'source': 'm_wait_timing_timing_accuracy_res', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_timing_timing_accuracy_res', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_timing_accuracy_req', 'source': 'm_initial', 'dest': 'm_send_timing_timing_accuracy_res'},
    {'trigger': 'send_timing_accuracy_res', 'source': 'm_send_timing_timing_accuracy_res', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_timing_timing_accuracy_res', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_timing_accuracy_req', 'source': 's_initial', 'dest': 's_wait_timing_timing_accuracy_res'},
    {'trigger': 'recv_timing_accuracy_res', 'source': 's_wait_timing_timing_accuracy_res', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_timing_timing_accuracy_res', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_timing_accuracy_req', 'source': 's_initial', 'dest': 's_send_timing_timing_accuracy_res'},
    {'trigger': 'send_timing_accuracy_res', 'source': 's_send_timing_timing_accuracy_res', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_timing_timing_accuracy_res', 'dest': 's_initial'},

    ### LMP_CLKOFFSET_REQ & LMP_CLKOFFSET_RES
    # Master
    {'trigger': 'send_clk_offset_req', 'source': 'm_initial', 'dest': 'm_wait_clkoffset_res'},
    {'trigger': 'recv_clk_offset_res', 'source': 'm_wait_clkoffset_res', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_clk_offset_req', 'source': 'm_initial', 'dest': 's_send_clkoffset_res'},
    {'trigger': 'send_clk_offset_res', 'source': 's_send_clkoffset_res', 'dest': 'm_initial'},

    ### LMP_VERSION_REQ/RES transaction
    # When: ANYTIME after baseband paging procedure
    # Master initiating
    {'trigger': 'send_version_req', 'source': 'm_initial', 'dest': 'm_wait_version_res'},
    {'trigger': 'recv_version_res', 'source': 'm_wait_version_res', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_version_req', 'source': 'm_initial', 'dest': 'm_send_version_res'},
    {'trigger': 'send_version_res', 'source': 'm_send_version_res', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_version_req', 'source': 's_initial', 'dest': 's_wait_version_res'},
    {'trigger': 'recv_version_res', 'source': 's_wait_version_res', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_version_req', 'source': 's_initial', 'dest': 's_send_version_res'},
    {'trigger': 'send_version_res', 'source': 's_send_version_res', 'dest': 's_initial'},

    ### LMP_FEATURES_REQ & LMP_FEATURES_RES
    # Master initiating
    {'trigger': 'send_features_req', 'source': 'm_initial', 'dest': 'm_wait_features_res'},
    {'trigger': 'recv_features_res', 'source': 'm_wait_features_res', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_features_req', 'source': 'm_initial', 'dest': 'm_send_features_features_res'},
    {'trigger': 'send_features_res', 'source': 'm_send_features_features_res', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_features_req', 'source': 's_initial', 'dest': 's_wait_features_res'},
    {'trigger': 'recv_features_res', 'source': 's_wait_features_res', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_features_req', 'source': 's_initial', 'dest': 's_send_features_features_res'},
    {'trigger': 'send_features_res', 'source': 's_send_features_features_res', 'dest': 's_initial'},

    ### LMP_FEATURES_REQ_EXT & LMP_FEATURES_RES_EXT
    ## May be performed after LMP_FEATURES_REQ/RES has been completed
    # Master initiating
    {'trigger': 'send_features_req_ext', 'source': 'm_initial', 'dest': 'm_wait_features_ext_res'},
    {'trigger': 'recv_features_ext_res', 'source': 'm_wait_features_ext_res', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_features_req_ext', 'source': 'm_initial', 'dest': 'm_send_features_ext_res'},
    {'trigger': 'send_features_ext_res', 'source': 'm_send_features_ext_res', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_features_req_ext', 'source': 's_initial', 'dest': 's_wait_features_ext_res'},
    {'trigger': 'recv_features_ext_res', 'source': 's_wait_features_ext_res', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_features_req_ext', 'source': 's_initial', 'dest': 's_send_features_ext_res'},
    {'trigger': 'send_features_ext_res', 'source': 's_send_features_ext_res', 'dest': 's_initial'},

    ### LMP_NAME_REQ & LMP_NAME_RES
    # When: ANYTIME after baseband paging procedure
    # Master initiating
    {'trigger': 'send_name_req', 'source': 'm_initial', 'dest': 'm_wait_name_res'},
    {'trigger': 'recv_name_res', 'source': 'm_wait_name_res', 'dest': 'm_initial'},
    # Master responsing
    {'trigger': 'recv_name_req', 'source': 'm_initial', 'dest': 'm_send_name_res'},
    {'trigger': 'send_name_res', 'source': 'm_send_name_res', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_name_req', 'source': 's_initial', 'dest': 's_wait_name_res'},
    {'trigger': 'recv_name_res', 'source': 's_wait_name_res', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_name_req', 'source': 's_initial', 'dest': 's_send_name_res'},
    {'trigger': 'send_name_res', 'source': 's_send_name_res', 'dest': 's_initial'},

    ### LMP_SLOT_OFFSET
    # Master
    {'trigger': 'send_slot_offset', 'source': 'm_initial', 'dest': 'm_initial'},
    {'trigger': 'recv_slot_offset', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'send_slot_offset', 'source': 's_initial', 'dest': 's_initial'},
    {'trigger': 'recv_slot_offset', 'source': 's_initial', 'dest': 's_initial'},

    ### LMP_SWITCH_REQ
    # Changes afh_reporting_mode to False when it succeeds
    # Master initiating
    {'trigger': 'send_switch_req', 'source': 'm_initial', 'dest': 'm_wait_switch_slot_offset'},
    {'trigger': 'recv_slot_offset', 'source': 'm_wait_switch_slot_offset', 'dest': 'm_wait_switch_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_switch_slot_offset', 'dest': 'm_initial'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_switch_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_switch_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_slot_offset', 'source': 'm_initial', 'dest': 'm_wait_switch_switch_req'},
    {'trigger': 'recv_switch_req', 'source': 'm_wait_switch_switch_req', 'dest': 'm_send_switch_accepted'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_switch_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_accepted', 'source': 'm_send_switch_accepted', 'dest': 's_initial'},
    # Slave initiating
    {'trigger': 'send_slot_offset', 'source': 's_initial', 'dest': 's_send_switch_switch_req'},
    {'trigger': 'send_switch_req', 'source': 's_send_switch_switch_req', 'dest': 's_wait_switch_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_switch_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_accepted', 'source': 's_wait_switch_accepted', 'dest': 'm_initial'},
    # Slave responding
    {'trigger': 'recv_switch_req', 'source': 's_initial', 'dest': 's_send_switch_slot_offset'},
    {'trigger': 'send_slot_offset', 'source': 's_send_switch_slot_offset', 'dest': 's_send_switch_accepted'},
    {'trigger': 'send_not_accepted', 'source': 's_send_switch_slot_offset', 'dest': 's_initial'},
    {'trigger': 'send_accepted', 'source': 's_send_switch_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_switch_accepted', 'dest': 's_initial'},

#### MODES OF OPERATION ####

    #### HOLD MODE

    ### LMP_HOLD
    ## Master forces LMP Hold Mode
    # The master may force Hold mode if there has previously been a request for Hold mode that has been accepted by the slave.
    {'trigger': 'send_hold', 'source': 'm_initial', 'dest': 'm_initial'},
    # Slave responding
    {'trigger': 'recv_hold', 'source': 's_initial', 'dest': 's_initial'},
    ## Slave forces LMP Hold Mode
    #The slave may force Hold mode if there has previously been a request for Hold mode that has been accepted by the master.
    {'trigger': 'send_hold', 'source': 's_initial', 'dest': 's_wait_hold_hold'},
    {'trigger': 'recv_hold', 'source': 's_wait_hold_hold', 'dest': 's_initial'},
    # Master responding
    {'trigger': 'recv_hold', 'source': 'm_initial', 'dest': 'm_wait_hold_hold'},
    {'trigger': 'send_hold', 'source': 'm_wait_hold_hold', 'dest': 'm_initial'},

    ### LMP_HOLD_REQ
    # Negotiates LMP Hold Mode
    # INCONSISTENCIES: Diagram indicates that minimum 3 LMP_HOLD_REQ must be transferred, text indicates minimum 1
    # Master initiating
    {'trigger': 'send_hold_req', 'source': 'm_initial', 'dest': 'm_wait_hold_req_decision'},
    {'trigger': 'recv_hold_req', 'source': 'm_wait_hold_req_decision', 'dest': 'm_send_hold_req_decision'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_hold_req_decision', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_hold_req_decision', 'dest': 'm_initial'},
    {'trigger': 'send_hold_req', 'source': 'm_send_hold_req_decision', 'dest': 'm_wait_hold_req_decision'},
    {'trigger': 'send_accepted', 'source': 'm_send_hold_req_decision', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_hold_req_decision', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_hold_req', 'source': 'm_initial', 'dest': 'm_send_res_hold_req_decision'},
    {'trigger': 'send_hold_req', 'source': 'm_send_res_hold_req_decision', 'dest': 'm_wait_res_hold_req_decision'},
    {'trigger': 'send_accepted', 'source': 'm_send_res_hold_req_decision', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_res_hold_req_decision', 'dest': 'm_initial'},
    {'trigger': 'recv_hold_req', 'source': 'm_wait_res_hold_req_decision', 'dest': 'm_send_res_hold_req_decision'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_res_hold_req_decision', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_res_hold_req_decision', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_hold_req', 'source': 's_initial', 'dest': 's_wait_hold_req_decision'},
    {'trigger': 'recv_hold_req', 'source': 's_wait_hold_req_decision', 'dest': 's_send_hold_req_decision'},
    {'trigger': 'recv_accepted', 'source': 's_wait_hold_req_decision', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_hold_req_decision', 'dest': 's_initial'},
    {'trigger': 'send_hold_req', 'source': 's_send_hold_req_decision', 'dest': 's_wait_hold_req_decision'},
    {'trigger': 'send_accepted', 'source': 's_send_hold_req_decision', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_hold_req_decision', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_hold_req', 'source': 's_initial', 'dest': 's_send_res_hold_req_decision'},
    {'trigger': 'send_hold_req', 'source': 's_send_res_hold_req_decision', 'dest': 's_wait_res_hold_req_decision'},
    {'trigger': 'send_accepted', 'source': 's_send_res_hold_req_decision', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_res_hold_req_decision', 'dest': 's_initial'},
    {'trigger': 'recv_hold_req', 'source': 's_wait_res_hold_req_decision', 'dest': 's_send_res_hold_req_decision'},
    {'trigger': 'recv_accepted', 'source': 's_wait_res_hold_req_decision', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_res_hold_req_decision', 'dest': 's_initial'},
    
    #### SNIFF MODE
    ### LMP_SNIFF_REQ
    # Very similar transaction to HOLD MODE requests
    # Master initiating
    {'trigger': 'send_sniff_req', 'source': 'm_initial', 'dest': 'm_wait_sniff_req_decision'},
    {'trigger': 'recv_sniff_req', 'source': 'm_wait_sniff_req_decision', 'dest': 'm_send_sniff_req_decision'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_sniff_req_decision', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_sniff_req_decision', 'dest': 'm_initial'},
    {'trigger': 'send_sniff_req', 'source': 'm_send_sniff_req_decision', 'dest': 'm_wait_sniff_req_decision'},
    {'trigger': 'send_accepted', 'source': 'm_send_sniff_req_decision', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_sniff_req_decision', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_sniff_req', 'source': 'm_initial', 'dest': 'm_send_res_sniff_req_decision'},
    {'trigger': 'send_sniff_req', 'source': 'm_send_res_sniff_req_decision', 'dest': 'm_wait_res_sniff_req_decision'},
    {'trigger': 'send_accepted', 'source': 'm_send_res_sniff_req_decision', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_res_sniff_req_decision', 'dest': 'm_initial'},
    {'trigger': 'recv_sniff_req', 'source': 'm_wait_res_sniff_req_decision', 'dest': 'm_send_res_sniff_req_decision'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_res_sniff_req_decision', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_res_sniff_req_decision', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_sniff_req', 'source': 's_initial', 'dest': 's_wait_sniff_req_decision'},
    {'trigger': 'recv_sniff_req', 'source': 's_wait_sniff_req_decision', 'dest': 's_send_sniff_req_decision'},
    {'trigger': 'recv_accepted', 'source': 's_wait_sniff_req_decision', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_sniff_req_decision', 'dest': 's_initial'},
    {'trigger': 'send_sniff_req', 'source': 's_send_sniff_req_decision', 'dest': 's_wait_sniff_req_decision'},
    {'trigger': 'send_accepted', 'source': 's_send_sniff_req_decision', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_sniff_req_decision', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_sniff_req', 'source': 's_initial', 'dest': 's_send_res_sniff_req_decision'},
    {'trigger': 'send_sniff_req', 'source': 's_send_res_sniff_req_decision', 'dest': 's_wait_res_sniff_req_decision'},
    {'trigger': 'send_accepted', 'source': 's_send_res_sniff_req_decision', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_res_sniff_req_decision', 'dest': 's_initial'},
    {'trigger': 'recv_sniff_req', 'source': 's_wait_res_sniff_req_decision', 'dest': 's_send_res_sniff_req_decision'},
    {'trigger': 'recv_accepted', 'source': 's_wait_res_sniff_req_decision', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_res_sniff_req_decision', 'dest': 's_initial'},

    ### LMP_UNSNIFF_REQ
    # Exit out of SNIFF MODE
    # Master initiating
    {'trigger': 'send_unsniff_req', 'source': 'm_initial', 'dest': 'm_wait_unsniff_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_unsniff_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_unsniff_req', 'source': 'm_initial', 'dest': 'm_send_unsniff_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_unsniff_accepted', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_unsniff_req', 'source': 's_initial', 'dest': 's_wait_unsniff_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_unsniff_accepted', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_unsniff_req', 'source': 's_initial', 'dest': 's_send_unsniff_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_unsniff_accepted', 'dest': 's_initial'},

    ### LMP_SNIFF_SUBRATING_REQ
    # Master initiating
    {'trigger': 'send_sniff_subrating_req', 'source': 'm_initial', 'dest': 'm_wait_subrating_res'},
    {'trigger': 'recv_sniff_subrating_res', 'source': 'm_wait_subrating_res', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_sniff_subrating_req', 'source': 'm_initial', 'dest': 'm_send_subrating_res'},
    {'trigger': 'send_sniff_subrating_res', 'source': 'm_send_subrating_res', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_sniff_subrating_req', 'source': 's_initial', 'dest': 's_wait_subrating_res'},
    {'trigger': 'recv_sniff_subrating_res', 'source': 's_wait_subrating_res', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_sniff_subrating_req', 'source': 's_initial', 'dest': 's_send_subrating_res'},
    {'trigger': 'send_sniff_subrating_res', 'source': 's_send_subrating_res', 'dest': 's_initial'},

#### LOGICAL TRANSPORTS ####
    #### SCO logical transport
    ### LMP_SCO_LINK_REQ
    # Master initiates
    {'trigger': 'send_sco_link_req', 'source': 'm_initial', 'dest': 'm_wait_sco_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_sco_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_sco_accepted', 'dest': 'm_initial'},
    # Slave responds
    {'trigger': 'recv_sco_link_req', 'source': 's_initial', 'dest': 's_send_res_sco_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_res_sco_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_res_sco_accepted', 'dest': 's_initial'},
    # Slave initiates
    {'trigger': 'send_sco_link_req', 'source': 's_initial', 'dest': 's_wait_sco_accepted'},
    {'trigger': 'recv_sco_link_req', 'source': 's_wait_sco_accepted', 'dest': 's_send_sco_accepted'},
    {'trigger': 'recv_not_accepted', 'source': 's_wait_sco_accepted', 'dest': 's_initial'},
    {'trigger': 'send_accepted', 'source': 's_send_sco_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_sco_accepted', 'dest': 's_initial'},
    # Master responds
    {'trigger': 'recv_sco_link_req', 'source': 'm_initial', 'dest': 'm_send_res_sco_accepted'},
    {'trigger': 'send_sco_link_req', 'source': 'm_send_res_sco_accepted', 'dest': 'm_wait_res_sco_accepted'},
    {'trigger': 'send_not_accepted', 'source': 'm_send_res_sco_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_res_sco_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_res_sco_accepted', 'dest': 'm_initial'},

    ### LMP_REMOVE_SCO_LINK_REQ
    # Master initiating
    {'trigger': 'send_remove_sco_link_req', 'source': 'm_initial', 'dest': 'm_wait_sco_remove_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_sco_remove_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_remove_sco_link_req', 'source': 'm_initial', 'dest': 'm_send_sco_remove_accepted'},
    {'trigger': 'send_accepted', 'source': 'm_send_sco_remove_accepted', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_remove_sco_link_req', 'source': 's_initial', 'dest': 's_wait_sco_remove_accepted'},
    {'trigger': 'recv_accepted', 'source': 's_wait_sco_remove_accepted', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_remove_sco_link_req', 'source': 's_initial', 'dest': 's_send_sco_remove_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_sco_remove_accepted', 'dest': 's_initial'},

    ### LMP_eSCO_LINK_REQ
    # For the eSCO link transactions there is an entire section describing rules for LMP negotiation and renegotiation.
    # Master initiates
    {'trigger': 'send_esco_link_req', 'source': 'm_initial', 'dest': 'm_wait_esco_accepted'},
    {'trigger': 'recv_esco_link_req', 'source': 'm_wait_esco_accepted', 'dest': 'm_send_esco_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_esco_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_esco_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_esco_link_req', 'source': 'm_send_esco_accepted', 'dest': 'm_wait_esco_accepted'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_esco_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_esco_accepted', 'dest': 'm_initial'},
    # Master responds
    {'trigger': 'recv_esco_link_req', 'source': 'm_initial', 'dest': 'm_wait_esco_res_accepted'},
    {'trigger': 'send_esco_link_req', 'source': 'm_wait_esco_res_accepted', 'dest': 'm_wait_res_esco_accepted'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_wait_esco_res_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_esco_link_req', 'source': 'm_wait_res_esco_accepted', 'dest': 'm_send_res_esco_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_res_esco_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_res_esco_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_esco_link_req', 'source': 'm_send_res_esco_accepted', 'dest': 'm_wait_res_esco_accepted'},
    {'trigger': 'send_not_accepted_ext', 'source': 'm_send_res_esco_accepted', 'dest': 'm_initial'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_res_esco_accepted', 'dest': 'm_initial'},
    # Slave initiates
    {'trigger': 'send_esco_link_req', 'source': 's_initial', 'dest': 's_wait_esco_initial_accepted'},
    {'trigger': 'recv_esco_link_req', 'source': 's_wait_esco_initial_accepted', 'dest': 's_send_esco_accepted'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_esco_initial_accepted', 'dest': 's_initial'},
    {'trigger': 'send_esco_link_req', 'source': 's_send_esco_accepted', 'dest': 's_wait_esco_accepted'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_esco_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 's_send_esco_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_esco_link_req', 'source': 's_wait_esco_accepted', 'dest': 's_send_esco_accepted'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_esco_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_esco_accepted', 'dest': 's_initial'},
    # Slave responds
    {'trigger': 'recv_esco_link_req', 'source': 's_initial', 'dest': 's_send_res_esco_accepted'},
    {'trigger': 'send_esco_link_req', 'source': 's_send_res_esco_accepted', 'dest': 's_wait_res_esco_accepted'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_res_esco_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 's_send_res_esco_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_esco_link_req', 'source': 's_wait_res_esco_accepted', 'dest': 's_send_res_esco_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_res_esco_accepted', 'dest': 's_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 's_wait_res_esco_accepted', 'dest': 's_initial'},

    ### LMP_REMOVE_eSCO_LINK_REQ
    # Master initiating
    {'trigger': 'send_remove_esco_link_req', 'source': 'm_initial', 'dest': 'm_wait_remove_esco_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_remove_esco_accepted', 'dest': 'm_initial'},
    # Master responding
    {'trigger': 'recv_remove_esco_link_req', 'source': 'm_initial', 'dest': 'm_send_remove_esco_accepted'},
    {'trigger': 'send_accepted_ext', 'source': 'm_send_remove_esco_accepted', 'dest': 'm_initial'},
    # Slave initiating
    {'trigger': 'send_remove_esco_link_req', 'source': 's_initial', 'dest': 's_wait_remove_esco_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 's_wait_remove_esco_accepted', 'dest': 's_initial'},
    # Slave responding
    {'trigger': 'recv_remove_esco_link_req', 'source': 's_initial', 'dest': 's_send_remove_esco_accepted'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_remove_esco_accepted', 'dest': 's_initial'},

#### TEST MODE ####
    ### LMP_TEST_ACTIVATE
    # Activate Test mode
    {'trigger': 'send_test_activate', 'source': 'm_initial', 'dest': 'm_wait_test_activate_accepted'},
    {'trigger': 'recv_accepted', 'source': 'm_wait_test_activate_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted', 'source': 'm_wait_test_activate_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_test_activate', 'source': 's_initial', 'dest': 's_send_test_activate_accepted'},
    {'trigger': 'send_accepted', 'source': 's_send_test_activate_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted', 'source': 's_send_test_activate_accepted', 'dest': 's_initial'},

    ### LMP_TEST_CONTROL
    {'trigger': 'send_test_control', 'source': 'm_initial', 'dest': 'm_wait_test_control_accepted'},
    {'trigger': 'recv_accepted_ext', 'source': 'm_wait_test_control_accepted', 'dest': 'm_initial'},
    {'trigger': 'recv_not_accepted_ext', 'source': 'm_wait_test_control_accepted', 'dest': 'm_initial'},
    # Slave
    {'trigger': 'recv_test_control', 'source': 's_initial', 'dest': 's_send_test_control_accepted'},
    {'trigger': 'send_accepted_ext', 'source': 's_send_test_control_accepted', 'dest': 's_initial'},
    {'trigger': 'send_not_accepted_ext', 'source': 's_send_test_control_accepted', 'dest': 's_initial'},

]

## type: GraphMachine
class LmpStateMachine(object):

    def __init__(self):
        self.machine = GraphMachine(model=self, states=states, transitions=transitions, initial='m_initial', title='LMP State Machine')
    
    def get_triggers(self):
        return self.machine.get_triggers(self.state)
    
    def get_state(self):
        return self.state
    

model = LmpStateMachine()
"""
Uncomment below to draw an image of the state machine.
Be sure to exclude/comment out transitions that are able to be send from any source to prevent large increase in image and file size. ('source': '*')
"""
#model.get_graph().draw('lmp_state_machine.png', prog='dot', format='png')