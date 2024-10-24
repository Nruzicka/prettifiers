import json
import xml.etree.cElementTree as ET


def pretty_print_xml(s: str) -> str:

    def parse_nested_xml(xml_element: ET.Element):
        for child in xml_element:
            # Handling elements with both text and xml nodes
            if child.text is not None and "<" in child.text and ">" in child.text:
                nested_xml = ET.fromstring(child.text)
                ET.indent(nested_xml)
                child.extend(nested_xml)
                child.text = None
            else:
                ET.indent(child)
            parse_nested_xml(child)
    
    xml_s = ET.XML(s)
    parse_nested_xml(xml_s)
    return ET.tostring(xml_s, encoding='unicode', method='xml')


def pretty_print_json(s: str) -> str:
    json_s = json.loads(s)
    return json.dumps(json_s, indent=4)

